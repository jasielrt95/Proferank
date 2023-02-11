let college = document.getElementById("college");
let other_college = document.getElementById("other_college");
let other_college_cont = document.getElementById("other_college_cont");

let department = document.getElementById("department");
let other_department = document.getElementById("other_department");
let other_department_cont = document.getElementById("other_department_cont");

// check if the values are other from the beginning
if (college.value == "Other") {
    other_college_cont.style.display = "flex";
} 
if (department.value == "Other") {
    other_department_cont.style.display = "flex";
}
college.addEventListener("change", function() {
    if (college.value == "Other") {
        other_college_cont.style.display = "flex";
    } else {
        other_college_cont.style.display = "none";
    }
});

department.addEventListener("change", function() {
    if (department.value == "Other") {
        other_department_cont.style.display = "flex";
    } else {
        other_department_cont.style.display = "none";
    }
});