let comment_toggle = document.getElementById("toggle-comment-form");

let comment_form = document.getElementById("comment-form");



comment_toggle.addEventListener("click", function() {
    comment_form.classList.toggle("hidden");
    comment_form.classList.toggle("flex");
    // toggle the text of the button
    comment_toggle.innerHTML = comment_toggle.innerHTML == "x" ? "+" : "x";
});

comment_form.addEventListener("submit", function() {
    comment_form.classList.toggle("hidden");
    comment_form.classList.toggle("flex");
    comment_toggle.innerHTML = comment_toggle.innerHTML == "+" ? "x" : "x";
});