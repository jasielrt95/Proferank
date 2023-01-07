function filterCollege() {
  var college = document.getElementById("college_filter").value;
  if (college == "") {
    return;
  }
  var professors = document.getElementsByClassName("professor");
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

function filterFaculty() {
  var faculty = document.getElementById("faculty_filter").value;
  if (faculty == "") {
    return;
  }
  var professors = document.getElementsByClassName("professor");
  for (var i = 0; i < professors.length; i++) {
    var professor = professors[i];
    var professor_faculty = professor.getAttribute("data-faculty");
    if (faculty == professor_faculty) {
      professor.style.display = "block";
    } else {
      professor.style.display = "none";
    }
  }
}

function filter() {
  var college = document.getElementById("college_filter").value;
  var faculty = document.getElementById("faculty_filter").value;
  if (college == "" && faculty == "") {
    return;
  }
  if (college == "") {
    filterFaculty();
    return;
  }
  if (faculty == "") {
    filterCollege();
    return;
  }
  var professors = document.getElementsByClassName("professor");
  for (var i = 0; i < professors.length; i++) {
    var professor = professors[i];
    var professor_college = professor.getAttribute("data-college");
    var professor_faculty = professor.getAttribute("data-faculty");
    if (college == professor_college && faculty == professor_faculty) {
      professor.style.display = "block";
    } else {
      professor.style.display = "none";
    }
  }
}

function search() {
  var search = document.getElementById("search-bar").value;
  var professors = document.getElementsByClassName("professor");
  for (var i = 0; i < professors.length; i++) {
    var professor = professors[i];
    var professor_name = professor.getAttribute("data-name");
    if (professor_name.toLowerCase().indexOf(search.toLowerCase()) > -1) {
      professor.style.display = "block";
    } else {
      professor.style.display = "none";
    }
  }
}

document.getElementById("college_filter").addEventListener("change", filter);
document.getElementById("faculty_filter").addEventListener("change", filter);
document.getElementById("search-bar").addEventListener("keyup", search);
