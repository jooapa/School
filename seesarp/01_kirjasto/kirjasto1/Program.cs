using kirjasto1.Models;
using System.Data.SqlClient;

public class DatabaseConnection
{
    private string _connectionString;

    public DatabaseConnection(string connectionString)
    {
        _connectionString = connectionString;
    }

    public string IsDbConnectionEstablished()
    {
        using var connection = new SqlConnection(_connectionString);

        try
        {
            connection.Open();
            return "Connection established!";
        }
        catch (SqlException ex)
        {
            throw;
        }

        catch (Exception ex)
        {
            throw;
        }
    }

    public List<User> GetAllUsers()
    {
        using var connection = new SqlConnection(_connectionString);
        connection.Open();

        using var command = new SqlCommand("SELECT * FROM Users", connection);
        using var reader = command.ExecuteReader();

        List<User> users = new List<User>();

        while (reader.Read())
        {
            User user = new User
            {
                Id = reader.GetInt32(0),
                FirstName = reader.GetString(1),
                LastName = reader.GetString(2),
                Address = reader.GetString(3),
                PhoneNumber = reader.GetString(4),
                Email = reader.GetString(5),
                RegistrationDate = reader.GetDateTime(6)
            };

            users.Add(user);
        }

        return users;
    }
}

public partial class Program
{
    public static void Main()
    {
        string connectionString =
            "Server=(localdb)\\MSSQLLocalDB;" +
            "Database=master;" +
            "Trusted_Connection=True;";

        //DatabaseConnection db = new DatabaseConnection(connectionString);
        //Console.WriteLine(db.IsDbConnectionEstablished());

        //List<User> users = db.GetAllUsers();
        //foreach (var user in users)
        //{
        //    Console.WriteLine(user.FirstName);
        //}

        //DataBaseRepository.GetBooksPublishedInLastFiveYears(connectionString);
        //DataBaseRepository.GetBookWithMostCopies(connectionString);
        //DataBaseRepository.GetMembersWhoHaveBorrowedBooks(connectionString);
        //DataBaseRepository.GetThreeMostBorrowedBooks(connectionString);

        DataBaseRepository repository = new();
        repository.GetBooksPublishedInLastFiveYears();
        repository.GetAverageAgeOfLibraryCustomers();
        repository.GetBookWithMostCopies();
        repository.GetMembersWhoHaveBorrowedBooks();

    }
}
