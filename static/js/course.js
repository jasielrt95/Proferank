let comment_toggle = document.getElementById("toggle-comment-form");
let edit_comment_toggle = document.getElementById("toggle-edit-comment-form");
console.log(edit_comment_toggle);

let comment_form = document.getElementById("comment-form");
let edit_comment_form = document.getElementById("edit-comment-form");

let comment_text = document.getElementById("comment-text");
let comment_submit = document.getElementById("submit-comment");


if (comment_toggle) {
    comment_text.addEventListener("keyup", validate_comment_form);

    comment_submit.disabled = true;
    comment_submit.classList.add("cursor-not-allowed");
    comment_submit.classList.add("bg-gray-400");
    comment_submit.classList.remove("bg-indigo-600");
    
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
};

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
