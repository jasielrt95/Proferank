function displayall() {
  var professors = document.getElementsByClassName("toggle");
  for (var i = 0; i < professors.length; i++) {
    var professor = professors[i];
    professor.style.display = "flex";
  }
}
function filterCollege() {
  var college = document.getElementById("college_filter").value;
  if (college == "") {
    return;
  }
  var professors = document.getElementsByClassName("toggle");
  for (var i = 0; i < professors.length; i++) {
    var professor = professors[i];
    var professor_college = professor.getAttribute("data-college");
    if (college == professor_college) {
      professor.style.display = "block";
    } else {
      professor.style.display = "none";
    }
  }
}

function filterdepartment() {
  var department = document.getElementById("department_filter").value;
  if (department == "") {
    return;
  }
  var professors = document.getElementsByClassName("toggle");
  for (var i = 0; i < professors.length; i++) {
    var professor = professors[i];
    var professor_department = professor.getAttribute("data-department");
    if (department == professor_department) {
      professor.style.display = "flex";
    } else {
      professor.style.display = "none";
    }
  }
}

function filter() {
  var college = document.getElementById("college_filter").value;
  var department = document.getElementById("department_filter").value;
  if (college == "" && department == "") {
    displayall();
  }
  if (college == "") {
    filterdepartment();
    return;
  }
  if (department == "") {
    filterCollege();
    return;
  }
  var professors = document.getElementsByClassName("toggle");
  for (var i = 0; i < professors.length; i++) {
    var professor = professors[i];
    var professor_college = professor.getAttribute("data-college");
    var professor_department = professor.getAttribute("data-department");
    if (college == professor_college && department == professor_department) {
      professor.style.display = "flex";
    } else {
      professor.style.display = "none";
    }
  }
}
function search() {
  var search = document.getElementById("search-bar").value;
  var courses = document.getElementsByClassName("toggle");
  for (var i = 0; i < courses.length; i++) {
    var course = courses[i];
    var course_name = course.getAttribute("data-name");
    var course_codification = course.getAttribute("data-codification");
    if (
      course_name.toLowerCase().indexOf(search.toLowerCase()) > -1 ||
      course_codification.toLowerCase().indexOf(search.toLowerCase()) > -1
    ) {
      course.style.display = "flex";
      console.log(course_name);
    } else {
      course.style.display = "none";
      console.log(course_name);
    }
  }
}

document.getElementById("college_filter").addEventListener("change", filter);
document.getElementById("department_filter").addEventListener("change", filter);
document.getElementById("search-bar").addEventListener("keyup", search);
