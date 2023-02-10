let edit_comment_toggle = document.getElementById("toggle-edit-comment-form");
let edit_comment_form = document.getElementById("edit-comment-form");
let edit_comment_submit = document.getElementById("submit-comment");
let edit_comment_text = document.getElementById("edit-comment-text");

if (edit_comment_toggle) {
    edit_comment_toggle.addEventListener("click", function() {
        edit_comment_form.classList.toggle("hidden");
        edit_comment_form.classList.toggle("flex");
        // toggle the text of the button
        edit_comment_toggle.innerHTML = edit_comment_toggle.innerHTML == "x" ? "📝" : "x";
    });

    edit_comment_form.addEventListener("submit", function() {
        edit_comment_form.classList.toggle("hidden");
        edit_comment_form.classList.toggle("flex");
        edit_comment_toggle.innerHTML = edit_comment_toggle.innerHTML == "x" ? "📝" : "x";
    });
}

function validate_comment_form() {
    edit_comment_submit.disabled = true;
    edit_comment_submit.classList.add("cursor-not-allowed");
    edit_comment_submit.classList.add("bg-gray-400");
    edit_comment_submit.classList.remove("bg-indigo-600");

    if (edit_comment_text.value == "") {
        edit_comment_submit.disabled = true;
        return;
    }
    else {
        edit_comment_submit.disabled = false;
        edit_comment_submit.classList.remove("cursor-not-allowed");
        edit_comment_submit.classList.remove("bg-gray-400");
        edit_comment_submit.classList.add("bg-indigo-600");
    }
}