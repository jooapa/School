#include <server.hh>
#include <http.hh>
#include <string>
#include <sstream>
#include <iostream>


_HTTP_REQUEST Server::parse_http_request(const std::string& request) {
    std::istringstream stream(request);
    _HTTP_REQUEST http_request;

    std::getline(stream, http_request.method, ' ');
    std::getline(stream, http_request.url, ' ');
    std::getline(stream, http_request.version);
    http_request.version.pop_back();

    // Parse the headers
    std::string header_line;
    while (std::getline(stream, header_line) && header_line != "\r") {
        size_t colon_pos = header_line.find(':');
        if (colon_pos != std::string::npos) {
            std::string key = header_line.substr(0, colon_pos);
            std::string value = header_line.substr(colon_pos + 1);
            value.erase(0, value.find_first_not_of(" "));
            value.pop_back();//last \r off
            http_request.headers[key] = value;
        }
    }

    //parse the body
    std::string body_line;
    while (std::getline(stream, body_line)) {
        http_request.body += body_line + "\n";
    }

    return http_request;
}



Server::Server(short port) {
    this->port = port;

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsa_data_) != 0) {
        throw std::runtime_error("WSAStartup failed");
    }

    // Create a socket
    listen_socket_ = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (listen_socket_ == INVALID_SOCKET) {
        WSACleanup();
        throw std::runtime_error("Socket creation failed");
    }

    // Set up the server address
    server_addr_.sin_family = AF_INET;
    server_addr_.sin_port = htons(port);
    server_addr_.sin_addr.s_addr = INADDR_ANY;

    // Bind the socket to the address
    if (bind(listen_socket_, reinterpret_cast<SOCKADDR*>(&server_addr_), sizeof(server_addr_)) == SOCKET_ERROR) {
        closesocket(listen_socket_);
        WSACleanup();
        throw std::runtime_error("Bind failed");
    }

    // Listen for incoming connections
    if (listen(listen_socket_, SOMAXCONN) == SOCKET_ERROR) {
        closesocket(listen_socket_);
        WSACleanup();
        throw std::runtime_error("Listen failed");
    }
}

Server::~Server() {
    closesocket(listen_socket_);
    WSACleanup();
}

void Server::start() {
    std::cout << "Server started. Listening on port " << this->port << "..." << std::endl;
    accept_connections();
}

size_t __send(SOCKET socket, const char* buffer, size_t length, int flags) {
    size_t total_sent = 0;
    while (total_sent < length) {
        size_t sent_bytes = send(socket, buffer + total_sent, length - total_sent, flags);
        if (sent_bytes == SOCKET_ERROR) {
            return sent_bytes;
        }
        total_sent += sent_bytes;
    }
    return total_sent;
}

void Server::accept_connections() {
    while (true) {
        SOCKET client_socket = accept(listen_socket_, nullptr, nullptr);
        if (client_socket == INVALID_SOCKET) {
            std::cerr << "Accept failed with error: " << WSAGetLastError() << std::endl;
            continue;
        }

        char buffer[4096] = {0};
        int bytes_received = recv(client_socket, buffer, sizeof(buffer) - 1, 0);
        if (bytes_received == SOCKET_ERROR) {
            std::cerr << "Error receiving data: " << WSAGetLastError() << std::endl;
            closesocket(client_socket);
            continue;
        }
        if(verbose)std::cout << "New connection established." << std::endl;

        // parse request
        std::string request_data(buffer, bytes_received);
        _HTTP_REQUEST http_request = parse_http_request(request_data);

        if(verbose)std::cout << "\nRequest received:" << std::endl;
        if(verbose)std::cout << "Method: " << http_request.method << "\n"
                  << "URL: " << http_request.url << "\n"
                  << "Version: " << http_request.version << "\n";
        if(verbose)
            for (const auto& [key, value] : http_request.headers) {
                std::cout << key << ": " << value << "\n";
            }
        if(verbose)std::cout << "Body: " << http_request.body << "\n";
        if(verbose)std::cout << "Request parsed.\n" << std::endl;

        if(http_request.method == "OPTIONS"){
            _HTTP_RESPONSE preflight_response = create_full_HTTP_RESPONSE_wide_params(
                HTTP_STATUS_CODE::OK,
                HTTP_VERSION::HTTP_1_1,
                HTTP_METHOD::OPTIONS,
                "",
                HTTP_CONTENT_TYPE::TEXT_PLAIN,
                http_request.url,
                "close",
                "localhost:"+std::to_string(this->port)
            );

            preflight_response.headers.content_length = "0";

            if(verbose)std::cout << "\nPreflight Response to send:" << std::endl;
            if(verbose)std::cout << preflight_response.format_to_string() << std::endl;

            size_t total_sent = __send(client_socket, preflight_response.format_and_to_c_str(), preflight_response.req_length(), 0);

            if(verbose)std::cout << "Preflight Response sent. " << total_sent << " bytes sent out of " << preflight_response.req_length() << " bytes." << std::endl;
        } else {
            _HTTP_RESPONSE response = create_full_HTTP_RESPONSE_wide_params(
                HTTP_STATUS_CODE::NOT_FOUND,
                HTTP_VERSION::HTTP_1_1,
                HTTP_METHOD::POST,
                "404 Not Found",
                HTTP_CONTENT_TYPE::TEXT_PLAIN,
                "/",
                "close",
                "localhost:"+std::to_string(this->port)
            );

            if(http_request.url == "/all"){
                if(verbose)std::cout << "get endpoint" << std::endl;
                get_all_nuke_facts(http_request, response);
            } else if(http_request.url == "/random"){
                if(verbose)std::cout << "get random endpoint" << std::endl;
                get_random_nuke_fact(http_request, response);
            } 
            

            if(verbose)std::cout << "\nResponse to send:" << std::endl;
            if(verbose)std::cout << response.format_to_string() << std::endl;
            if(verbose)std::cout << std::endl;
            size_t total_sent = __send(client_socket, response.format_and_to_c_str(), response.req_length(), 0);
        
            if(verbose)std::cout << "Response sent. " << total_sent << " bytes sent out of " << response.req_length() << " bytes." << std::endl;

            // Close the client socket after communication
        }
        closesocket(client_socket);
        if(verbose)std::cout <<"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
    }

}
