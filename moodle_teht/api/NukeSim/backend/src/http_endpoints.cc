#include <http.hh>
#include <database.hh>
#include <json.hpp>
#include <server.hh>
#include <crypt.hh>
#include <fstream>
#define INCLUDE_ATRC_STDLIB 1
#include <ATRC.hpp>
using json = nlohmann::json;
using namespace nlohmann::literals;

json response_json = json::parse(std::ifstream("nuke_facts.json"));

// api to get random string
void get_all_nuke_facts(_HTTP_REQUEST &request, _HTTP_RESPONSE &response)
{
    try
    {
        response = create_full_HTTP_RESPONSE_wide_params(
            HTTP_STATUS_CODE::OK,
            HTTP_VERSION::HTTP_1_1,
            HTTP_METHOD::GET,
            response_json.dump(),
            HTTP_CONTENT_TYPE::APPLICATION_JSON, // Changed to JSON content type
            "/",
            "close",
            "localhost:" + port);
    }
    catch (const std::exception &e)
    {
        exception_return(response, e);
    }
}

void get_random_nuke_fact(_HTTP_REQUEST &request, _HTTP_RESPONSE &response)
{
    // Get a random fact from the response_json
    // {
    // "facts": [
    //     {
    //         "id": 1,
    //         "fact": "The first nuclear bomb was dropped on Hiroshima, Japan on August 6, 1945."
    //     },

    try
    {
        // get the id of the random fact and get the fact
        int random_id = rand() % response_json["facts"].size();
        json random_fact = response_json["facts"][random_id];

        response = create_full_HTTP_RESPONSE_wide_params(
            HTTP_STATUS_CODE::OK,
            HTTP_VERSION::HTTP_1_1,
            HTTP_METHOD::GET,
            random_fact.dump(),
            HTTP_CONTENT_TYPE::APPLICATION_JSON, // Changed to JSON content type
            "/",
            "close",
            "localhost:" + port);
    }
    catch (const std::exception &e)
    {
        exception_return(response, e);
    }
}

void exception_return(_HTTP_RESPONSE &response, const std::exception &e)
{
    response = create_full_HTTP_RESPONSE_wide_params(
        HTTP_STATUS_CODE::INTERNAL_SERVER_ERROR,
        HTTP_VERSION::HTTP_1_1,
        HTTP_METHOD::GET,
        e.what(),
        HTTP_CONTENT_TYPE::TEXT_PLAIN,
        "/",
        "close",
        "localhost:" + port);
}

void verify_endpoint(_HTTP_REQUEST& request, _HTTP_RESPONSE& response) {
    try {

    } catch (const std::exception& e) {
        std::cerr << "Failed to verify user: " << e.what() << std::endl;
    }
}

void refresh_endpoint(_HTTP_REQUEST& request, _HTTP_RESPONSE& response) {
    try {

    } catch (const std::exception& e) {
        std::cerr << "Failed to refresh user: " << e.what() << std::endl;
    }
}

void update_endpoint(_HTTP_REQUEST& request, _HTTP_RESPONSE& response) {
    try {

    } catch (const std::exception& e) {
        std::cerr << "Failed to update user: " << e.what() << std::endl;
    }
}

void delete_endpoint(_HTTP_REQUEST& request, _HTTP_RESPONSE& response) {
    try {

    } catch (const std::exception& e) {
        std::cerr << "Failed to delete user: " << e.what() << std::endl;
    }
}

void get_endpoint(_HTTP_REQUEST& request, _HTTP_RESPONSE& response) {
    try {

    } catch (const std::exception& e) {
        std::cerr << "Failed to get user: " << e.what() << std::endl;
    }
}