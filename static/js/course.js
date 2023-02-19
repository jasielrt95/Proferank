let comment_toggle = document.getElementById("toggle-comment-form");
let edit_comment_toggle = document.getElementById("toggle-edit-comment-form");
console.log(edit_comment_toggle);

let comment_form = document.getElementById("comment-form");
let edit_comment_form = document.getElementById("edit-comment-form");

let comment_text = document.getElementById("comment-text");
let comment_submit = document.getElementById("submit-comment");

let codification_toggle = document.getElementById(
  "toggle-course-codification-form"
);
let codification_form = document.getElementById("course-codification-form");
let course_code = document.getElementById("course-code");
let codification_submit = document.getElementById("submit-course-codification");
let codification_error = document.getElementById("course-codification-error");

if (comment_toggle) {
  comment_text.addEventListener("keyup", validate_comment_form);

  comment_submit.disabled = true;
  comment_submit.classList.add("cursor-not-allowed");
  comment_submit.classList.add("bg-gray-400");
  comment_submit.classList.remove("bg-indigo-600");

  comment_toggle.addEventListener("click", function () {
    comment_form.classList.toggle("hidden");
    comment_form.classList.toggle("flex");
    // toggle the text of the button
    comment_toggle.innerHTML = comment_toggle.innerHTML == "x" ? "+" : "x";
  });

  comment_form.addEventListener("submit", function () {
    comment_form.classList.toggle("hidden");
    comment_form.classList.toggle("flex");
    comment_toggle.innerHTML = comment_toggle.innerHTML == "+" ? "x" : "x";
  });
}

if (edit_comment_toggle) {
  edit_comment_toggle.addEventListener("click", function () {
    edit_comment_form.classList.toggle("hidden");
    edit_comment_form.classList.toggle("flex");
    // toggle the text of the button
    edit_comment_toggle.innerHTML =
      edit_comment_toggle.innerHTML == "x" ? "📝" : "x";
  });

  edit_comment_form.addEventListener("submit", function () {
    edit_comment_form.classList.toggle("hidden");
    edit_comment_form.classList.toggle("flex");
    edit_comment_toggle.innerHTML =
      edit_comment_toggle.innerHTML == "x" ? "📝" : "x";
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
  } else {
    comment_submit.disabled = false;
    comment_submit.classList.remove("cursor-not-allowed");
    comment_submit.classList.remove("bg-gray-400");
    comment_submit.classList.add("bg-indigo-600");
  }
}

if (codification_toggle) {
  codification_submit.disabled = true;
  codification_submit.classList.add("cursor-not-allowed");
  codification_submit.classList.add("bg-gray-400");
  codification_submit.classList.remove("bg-indigo-600");

  codification_toggle.addEventListener("click", function () {
    codification_form.classList.toggle("hidden");
    codification_form.classList.toggle("flex");
    codification_error.innerHTML = "";
    codification_toggle.innerHTML =
      codification_toggle.innerHTML == "x" ? "añadir codificación" : "x";
  });
  codification_form.addEventListener("submit", function () {
    codification_form.classList.toggle("hidden");
    codification_form.classList.toggle("flex");
    codification_toggle.innerHTML =
      codification_toggle.innerHTML == "X" ? "X" : "X";
  });
  course_code.addEventListener("keyup", validate_codification_form);
}

function validate_codification_form() {
  if (course_code.value == "") {
    codification_submit.disabled = true;
    codification_submit.classList.add("cursor-not-allowed");
    codification_submit.classList.add("bg-gray-400");
    codification_submit.classList.remove("bg-indigo-600");
    return;
  }
  if (
    !course_code.value.match(/^[A-Z]{4}[0-9]{4}$/) ||
    course_code.value.includes(" ")
  ) {
    codification_submit.disabled = true;
    codification_submit.classList.add("cursor-not-allowed");
    codification_submit.classList.add("bg-gray-400");
    codification_submit.classList.remove("bg-indigo-600");
    // if the first four characters are not uppercase letters
    if (!course_code.value.match(/^[A-Z]{4}/)) {
      codification_error.innerHTML =
        "El código del curso debe comenzar con cuatro letras mayúsculas";
      return;
    }
    // if the last four characters are not numbers
    if (!course_code.value.match(/[0-9]{4}$/)) {
      codification_error.innerHTML =
        "El código del curso debe terminar con cuatro números";
      return;
    }
    // if the course code contains spaces
    if (course_code.value.includes(" ")) {
      codification_error.innerHTML =
        "El código del curso no debe contener espacios";
      return;
    }
  }
  codification_submit.disabled = false;
  codification_submit.classList.remove("cursor-not-allowed");
  codification_submit.classList.remove("bg-gray-400");
  codification_submit.classList.add("bg-indigo-600");
  codification_error.innerHTML = "";
}
