using System.ComponentModel.DataAnnotations;

namespace Networking.Models
{
    public class DatabaseEnter
    {
        [Required]
        [MinLength(4)]
        [Display(Name = "First Name:")]
        public string Firstname {get; set;}
        [Required]
        [MinLength(4)]
        [Display(Name = "Last Name:")]
        public string Lastname {get; set;}
        [Required]
        [EmailAddress]
        [Display(Name = "Email:")]
        public string Email {get; set;}
        [Required]
        [DataType(DataType.Password)]
        [MinLength(8)]
        [Display(Name = "Password:")]
        public string Password {get; set;}
        [Required]
        [DataType(DataType.Password)]
        [Display(Name = "Confirm Password:")]

        public string Confirm {get; set;}
        [Required]
        [DataType(DataType.Date)]
        [Display(Name = "Your Age:")]
        public int Age {get; set;}

    }
}