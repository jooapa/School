//using Microsoft.Data.SqlClient;
using Konscious.Security.Cryptography;
//namespace EventCalander
//{
//    public class Api
//    {
//        /// <summary>
//        /// add event to database
//        /// </summary>
//        public void AddEvent(Event @event)
//        {
//            // create connection
//            using var connection = new SqlConnection("Server=localhost;Database=EventCalander;Trusted_Connection=True;");
//            connection.Open();

//            // create command
//            using var command = connection.CreateCommand();
//            command.CommandText = "INSERT INTO Events (Title, Description, StartDate, EndDate, Location, CategoryId, CreatedBy) VALUES (@Title, @Description, @StartDate, @EndDate, @Location, @CategoryId, @CreatedBy)";
//            command.Parameters.AddWithValue("@Title", @event.Title);
//            command.Parameters.AddWithValue("@Description", @event.Description);
//            command.Parameters.AddWithValue("@StartDate", @event.StartDate);
//            command.Parameters.AddWithValue("@EndDate", @event.EndDate);
//            command.Parameters.AddWithValue("@Location", @event.Location);
//            command.Parameters.AddWithValue("@CategoryId", @event.CategoryId);
//            command.Parameters.AddWithValue("@CreatedBy", @event.CreatedBy);

//            // execute command
//            command.ExecuteNonQuery();
//            connection.Close();
//        }
//    }
//}

using Microsoft.EntityFrameworkCore;
using System.Diagnostics;

namespace EventCalander
{
    public class Api
    {
        private readonly ApplicationDbContext _context;

        public Api(ApplicationDbContext context)
        {
            _context = context;
        }

        public async Task AddEvent(Event @event)
        {
            // Add the event to the database context
            _context.Events.Add(@event);

            // Save the changes to the database
            await _context.SaveChangesAsync();
        }

        public async Task UpdateEvent(Event @event)
        {
            // Update the event in the database context
            _context.Events.Update(@event);

            // Save the changes to the database
            await _context.SaveChangesAsync();
        }

        public async Task<IEnumerable<Category>> GetCategories()
        {
            var cat = await _context.Categories.ToListAsync();
            //foreach (var c in cat)
            //{
            //    Debug.WriteLine(c.Name + c.Id);
            //}
            return cat;
        }

        public async Task<IEnumerable<User>> GetUsers()
        {
            return await _context.Users.ToListAsync();
        }

        public async Task<IEnumerable<Event>> GetEvents()
        {
            return await _context.Events.ToListAsync();
        }

		/// <summary>
        /// has password
        /// </summary>
        public string HashPassword(string password)
		{
			// Hash the password
			Argon2id argon2 = new(System.Text.Encoding.UTF8.GetBytes(password))
			{
				Salt = System.Text.Encoding.UTF8.GetBytes("salt"),
				MemorySize = 65536,
				DegreeOfParallelism = 4,
				Iterations = 4
			};
			byte[] hash = argon2.GetBytes(16);

			// Convert the hash to a string
			return Convert.ToBase64String(hash);
		}

		/// <summary>
		/// login
		/// </summary
		public async Task<string> Login(string email, string pass)
		{
			// Hash the password
			string passwordHash = HashPassword(pass);

			// Find the user in the database
			User? dbUser = await _context.Users.FirstOrDefaultAsync(u => u.Email == email);

			// Check if the user exists
			if (dbUser == null)
			{
				return "User not found";
			}

			// Check if the password is correct
			if (dbUser.PasswordHash != passwordHash)
			{
				return "Incorrect password";
			}

			return "Login successful";
		}

		/// <summary>
		/// sign up
		/// </summary
		public async Task SignUp(User user)
        {
            user.PasswordHash = HashPassword(user.PasswordHash);

			// if admin
			if(user.FirstName == "admin")
			{
				user.Role = "admin";
			}
			else
			{
				user.Role = "user";
			}

			_context.Users.Add(user);

			await _context.SaveChangesAsync();

		}
	}
}

