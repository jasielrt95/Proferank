let course_toggle = document.getElementById("toggle-course-form");
let course_form = document.getElementById("course-form");
course_toggle.addEventListener("click", function () {
  course_form.classList.toggle("hidden");
  course_form.classList.toggle("flex");
  // toggle the text of the button
  course_toggle.innerHTML = course_toggle.innerHTML == "x" ? "+" : "x";
});


// Form validation
let course_name = document.getElementById("course-name");
let course_code = document.getElementById("course-code");
let course_form_submit = document.getElementById("course-form-submit");
let course_form_error = document.getElementById("course-form-error");

// Add event listeners to the form elements
course_name.addEventListener("keyup", validate_course_form);
course_code.addEventListener("keyup", validate_course_form);

// disable the submit button by default


function validate_course_form() {
  course_form_submit.disabled = true;
  course_form_submit.classList.add("cursor-not-allowed");
  course_form_submit.classList.add("bg-gray-400");
  course_form_submit.classList.remove("bg-indigo-600");
  // Check if the course name is empty
  if (course_name.value == "") {
    course_form_submit.disabled = true;
    course_form_error.innerHTML = "El nombre del curso no puede estar vacío";
    return;
  }

  // Check if the course code is empty
  if (course_code.value == "") {
    course_form_submit.disabled = true;
    course_form_error.innerHTML = "El código del curso no puede estar vacío";
    return;
  }

  // Check if the course code is valid
  if (!course_code.value.match(/^[A-Z]{4}[0-9]{4}$/)) {
    course_form_submit.disabled = true;
    course_form_error.innerHTML = "El código del curso no es válido";
    return;
  }

  // If all the checks pass, enable the submit button
  course_form_submit.disabled = false;

  // remove the error message
  course_form_error.innerHTML = "";

  // Remove the cursor-not-allowed class from the submit button
  course_form_submit.classList.remove("cursor-not-allowed");

  // Change the color to bg-indigo-600
  course_form_submit.classList.add("bg-indigo-600");
  course_form_submit.classList.remove("bg-gray-400");
}