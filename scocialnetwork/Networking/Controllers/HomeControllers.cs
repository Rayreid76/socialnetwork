using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Networking.Models;
namespace Networking.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index() => View();

        [HttpGet("Registure")]
        public IActionResult Registure() => View();

        [HttpGet("Login")]
        public IActionResult Login() => View();

        [HttpGet("Dashboard")]
        public IActionResult Dashboard() => View();

        [HttpPost("Create")]
        public IActionResult Create(DatabaseEnter user)
        {
            if(ModelState.IsValid)
            {
                return RedirectToAction("Login");
            }
            else
            {
                return View("Registure");
            }
            
        }
        [HttpPost("loginto")]
        public IActionResult Loginto(DatabaseEnter user)
        {
            if(ModelState.IsValid)
            {
                return RedirectToAction("Dashboard");
            }
            else
            {
                return View("Login");

            }
        }
    }
}