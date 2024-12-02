using EventCalander;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

namespace EventCalander
{
	public class Event
	{
		[Key]
		public int Id { get; set; }
        [Required(ErrorMessage = "Title is required")]
        [StringLength(100, ErrorMessage = "Title cannot exceed 100 characters")]
        public string Title { get; set; }
        [Required(ErrorMessage = "Description is required")]
        public string Description { get; set; }
		[Required(ErrorMessage = "Start Date is required")]
		public DateTime? StartDate { get; set; }
        [Required(ErrorMessage = "End Date is required")]
        public DateTime? EndDate { get; set; }
        [Required(ErrorMessage = "Location is required")]
        public string Location { get; set; }
        [Required(ErrorMessage = "Category is required")]
        [DeniedValues(0, ErrorMessage = "Please select a valid category.")]
        public int CategoryId { get; set; }
		public int CreatedBy { get; set; }
	}

	public class Category
	{
		[Key]
		public int Id { get; set; }
		public string Name { get; set; }
		public string Description { get; set; }
	}

	public class User
	{
		[Key]
		public int Id { get; set; }
		[Required(ErrorMessage = "First Name is required")]
		public string FirstName { get; set; }
		[Required(ErrorMessage = "Last Name is required")]
		public string LastName { get; set;  }
		[Required(ErrorMessage = "Email is required")]
		public string Email { get; set; }
		[Required(ErrorMessage = "Password is required")]
		public string PasswordHash { get; set; }
		[Required(ErrorMessage = "Role is required")]
		public string Role { get; set; }
	}
}

