let tasks = [];

function addTask() {

    const input = document.getElementById("taskInput");

    const text = input.value.trim();

    if(text === ""){
        alert("Please enter a task.");
        return;
    }

    tasks.push({
        text: text,
        completed: false
    });

    input.value = "";

    displayTasks();
}

function displayTasks(filter = "all") {

    const list = document.getElementById("taskList");

    list.innerHTML = "";

    let filtered = tasks;

    if(filter === "completed"){
        filtered = tasks.filter(task => task.completed);
    }

    if(filter === "pending"){
        filtered = tasks.filter(task => !task.completed);
    }

    filtered.forEach((task,index)=>{

        const li = document.createElement("li");

        li.innerHTML = `
        <span
            class="task-text ${task.completed ? "completed":""}"
            onclick="toggleTask(${tasks.indexOf(task)})">
            ${task.text}
        </span>

        <button
            class="delete-btn"
            onclick="deleteTask(${tasks.indexOf(task)})">
            Delete
        </button>
        `;

        list.appendChild(li);

    });

    document.getElementById("totalTasks").textContent = tasks.length;
}

function toggleTask(index){

    tasks[index].completed = !tasks[index].completed;

    displayTasks();
}

function deleteTask(index){

    tasks.splice(index,1);

    displayTasks();
}

function filterTasks(type){

    displayTasks(type);

}
