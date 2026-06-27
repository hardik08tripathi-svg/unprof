// Array to store students
let students = [];

// Add Student
function addStudent() {

    const name = document.getElementById("name").value;
    const mark1 = Number(document.getElementById("mark1").value);
    const mark2 = Number(document.getElementById("mark2").value);
    const mark3 = Number(document.getElementById("mark3").value);

    if(name === "" || isNaN(mark1) || isNaN(mark2) || isNaN(mark3)){
        alert("Please enter all details.");
        return;
    }

    const average = ((mark1 + mark2 + mark3) / 3).toFixed(2);

    const status = average >= 40 ? "Pass" : "Fail";

    // Student Object
    const student = {
        name,
        mark1,
        mark2,
        mark3,
        average,
        status
    };

    // Store in Array
    students.push(student);

    displayStudents();

    // Clear Inputs
    document.getElementById("name").value = "";
    document.getElementById("mark1").value = "";
    document.getElementById("mark2").value = "";
    document.getElementById("mark3").value = "";
}

// Display Students
function displayStudents(){

    const table = document.getElementById("studentTable");

    table.innerHTML = "";

    students.forEach(student => {

        table.innerHTML += `
        <tr>
            <td>${student.name}</td>
            <td>${student.mark1}</td>
            <td>${student.mark2}</td>
            <td>${student.mark3}</td>
            <td>${student.average}</td>
            <td class="${student.status === "Pass" ? "pass" : "fail"}">
                ${student.status}
            </td>
        </tr>
        `;

    });

}
