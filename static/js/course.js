let comment_toggle = document.getElementById("toggle-comment-form");

let comment_form = document.getElementById("comment-form");

let comment_text = document.getElementById("comment-text");
let comment_submit = document.getElementById("submit-comment");



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

comment_text.addEventListener("keyup", validate_comment_form);

comment_submit.disabled = true;
comment_submit.classList.add("cursor-not-allowed");
comment_submit.classList.add("bg-gray-400");
comment_submit.classList.remove("bg-indigo-600");

function validate_comment_form() {
    comment_submit.disabled = true;
    comment_submit.classList.add("cursor-not-allowed");
    comment_submit.classList.add("bg-gray-400");
    comment_submit.classList.remove("bg-indigo-600");

    if (comment_text.value == "") {
        comment_submit.disabled = true;
        return;
    }
    else {
        comment_submit.disabled = false;
        comment_submit.classList.remove("cursor-not-allowed");
        comment_submit.classList.remove("bg-gray-400");
        comment_submit.classList.add("bg-indigo-600");
    }
}
