using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Data.SqlClient;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;
using Microsoft.EntityFrameworkCore;

namespace kirjasto1.Models
{
    public class DataBaseRepository
    {
        // - Tee DataBaseRepository.cs luokkaan metodit, jotka tekevät alla olevat toiminnot.Huom!
        // Voit kokeilla SQL-kyselyjen toimivuutta suoraan kantaa vasten ja
        // vasta sen jälkeen siirtää kyselyn C#-koodiin.
        // Alla olevissa tehtävissä tulee hakea tietoa tietokannasta ja
        // tallentaa ne olioihin (Book, Loan, User):

        // - Hae kaikki kirjat, jotka on julkaistu viiden vuoden sisällä.
        // Tulosta kirjat konsoliin.

        // - Hae kirjaston asiakkaiden keski-ikä.Tulosta keski-ikä konsoliin.
        // Jos ikää ei ole, niin lisää syntymäaika tietokantaan.

        // - Hae kirja, joita on eniten tarjolla kirjastossa.
        // Tulosta kirjan nimi konsoliin.

        // - Hae jäsenet, jotka lainasivat ainakin yhden kirjan kirjastosta.
        // Tulosta jäsenen nimi ja kirjan ISBN konsoliin.

        // - (Bonus) Hae kolmen lainatuimman kirjan kaikki tiedot konsoliin.
        // Vihje! Tarvitset useamman Join-lauseen.

        public static void GetBooksPublishedInLastFiveYears(string connection)
        {
            using SqlConnection conn = new SqlConnection(connection);
            conn.Open();
            using SqlCommand cmd = new("SELECT * FROM Book WHERE PublicationYear >= YEAR(GETDATE()) - 5", conn);
            using SqlDataReader reader = cmd.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    Console.WriteLine(reader.GetString(1));
                }
            }
            else
            {
                Console.WriteLine("No books published within the last 5 years");
            }
        }

        public static void GetAverageAgeOfLibraryCustomers(string connection)
        {
            using SqlConnection conn = new SqlConnection(connection);
            conn.Open();
            using SqlCommand cmd = new("SELECT AVG(DATEDIFF(YEAR, BirthDate, GETDATE())) FROM Users", conn);
            using SqlDataReader reader = cmd.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    Console.WriteLine(reader.GetInt32(0));
                }
            }
            else
            {
                Console.WriteLine("No age data available");
            }
        }

        public static void GetBookWithMostCopies(string connection)
        {
            using SqlConnection conn = new SqlConnection(connection);
            conn.Open();
            using SqlCommand cmd = new("SELECT TOP 1 Title FROM Book ORDER BY AvailableCopies DESC", conn);
            using SqlDataReader reader = cmd.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    Console.WriteLine(reader.GetString(0));
                }
            }
            else
            {
                Console.WriteLine("No books available");
            }
        }

        public static void GetMembersWhoHaveBorrowedBooks(string connection)
        {
            using SqlConnection conn = new SqlConnection(connection);
            conn.Open();
            using SqlCommand cmd = new("SELECT Users.FirstName, Book.ISBN FROM Users JOIN Loan ON Users.MemberId = Loan.MemberId JOIN Book ON Loan.BookId = Book.BookId", conn);
            using SqlDataReader reader = cmd.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    Console.WriteLine(reader.GetString(0) + " " + reader.GetString(1));
                }
            }
            else
            {
                Console.WriteLine("No books borrowed");
            }
        }

        public static void GetThreeMostBorrowedBooks(string connection)
        {
            using SqlConnection conn = new SqlConnection(connection);
            conn.Open();
            using SqlCommand cmd = new("SELECT TOP 3 Book.Title, COUNT(Loan.BookId) FROM Book JOIN Loan ON Book.BookId = Loan.BookId GROUP BY Book.Title ORDER BY COUNT(Loan.BookId) DESC", conn);
            using SqlDataReader reader = cmd.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    Console.WriteLine(reader.GetString(0) + " " + reader.GetInt32(1));
                }
            }
            else
            {
                Console.WriteLine("No books borrowed");
            }
        }

        // - Tee seuraavat kyselyt käyttäen LINQ-kirjastoa.Nyt voisi olla myös hyvä hetki ainakin käydä katsomassa https://learn.microsoft.com/en-us/ef/core/ ja miettiä voisinko itse käyttää kyseistä frameworkkia hyväkseni.

        // - Hae kaikki kirjat, jotka on julkaistu 10 vuoden sisällä.Tulosta kirjat konsoliin.
        // - Hae kirjaston asiakkaiden korkein ikä.Tulosta korkein ikä ja asiakkaan nimi konsoliin.
        // - Hae kirja, joita on vähiten tarjolla kirjastossa.Tulosta kirjan nimi konsoliin.
        // - Hae jäsenet, jotka eivät lainanneet yhtään kirjaa kirjastosta. Tulosta jäsenen nimi konsoliin.
        // - (Bonus) Hae kolmen lainatuimman kirjan julkaisuvuosi. Tulosta julkaisuvuosi konsoliin.

        // ESIMERKKI:
        // private static void GetBooksByVilleQuerySyntas()
        // {
        //     using var context = new LibaryContext();
        //     var books = context.Books.ToList();
        //     var booksOfVille = from book in books where book.Title.Contains("Ville") select book;
        // }

        public void GetBooksPublishedInLastFiveYears()
        {
            using var context = new LibraryContext();
            var books = context.Books.ToList();
            var booksPublishedInLastFiveYears = from book in books where book.PublicationYear >= DateTime.Now.Year - 5 select book;

            if (booksPublishedInLastFiveYears.Any())
            {
                foreach (var book in booksPublishedInLastFiveYears)
                {
                    Console.WriteLine(book.Title);
                }
            }
            else
            {
                Console.WriteLine("No books published within the last 5 years");
            }
        }

        public void GetAverageAgeOfLibraryCustomers()
        {
            using var context = new LibraryContext();
            var users = context.Users.ToList();
            var averageAge = users.Average(user => user.RegistrationDate != null ? DateTime.Now.Year - user.RegistrationDate.Year : 0);

            if (averageAge != 0)
            {
                Console.WriteLine(averageAge);
            }
            else
            {
                Console.WriteLine("No age data available");
            }
        }

        public void GetBookWithMostCopies()
        {
            using var context = new LibraryContext();
            var books = context.Books.ToList();
            var bookWithMostCopies = books.OrderByDescending(book => book.AvailableCopies).FirstOrDefault();

            if (bookWithMostCopies != null)
            {
                Console.WriteLine(bookWithMostCopies.Title);
            }
            else
            {
                Console.WriteLine("No books available");
            }
        }

        public void GetMembersWhoHaveBorrowedBooks()
        {
            using var context = new LibraryContext();
            var users = context.Users.ToList();
            var loans = context.Loans.ToList();
            var books = context.Books.ToList();

            var membersWhoHaveBorrowedBooks = from user in users
                                              join loan in loans on user.Id equals loan.MemberId
                                              join book in books on loan.BookId equals book.Id
                                              select new { user.FirstName, book.ISBN };

            if (membersWhoHaveBorrowedBooks.Any())
            {
                foreach (var member in membersWhoHaveBorrowedBooks)
                {
                    Console.WriteLine(member.FirstName + " " + member.ISBN);
                }
            }
            else
            {
                Console.WriteLine("No books borrowed");
            }
        }
    }
}
