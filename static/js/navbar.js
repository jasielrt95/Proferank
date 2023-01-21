let hamburger = document.getElementById("mobile-hamburger");
let menu = document.getElementById("mobile-menu");
let hamburger_lines = document.getElementsByClassName("hamburger-line");

hamburger.addEventListener("click", function () {
  console.log("clicked");
  menu.classList.toggle("hidden");
  for (let i = 0; i < hamburger_lines.length; i++) {
    hamburger_lines[i].classList.toggle("animate-pulse");
  }
});
