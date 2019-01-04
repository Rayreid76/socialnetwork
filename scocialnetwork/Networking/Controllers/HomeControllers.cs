using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
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
    }
}