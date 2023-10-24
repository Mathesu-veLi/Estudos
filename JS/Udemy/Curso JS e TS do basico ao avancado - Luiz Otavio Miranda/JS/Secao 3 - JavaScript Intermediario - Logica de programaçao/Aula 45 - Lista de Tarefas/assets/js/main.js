const inputTask = document.querySelector('.input-new-task');
const btnTask = document.querySelector('.btn-new-task');
const tasks = document.querySelector('.tasks');

inputTask.addEventListener('keypress', function (event) {
    if (event.keyCode === 13) {
        createTask(inputTask.value);
        inputTask.value = '';
    }
})

btnTask.addEventListener('click', function (event) {
    createTask(inputTask.value);
    inputTask.value = '';
})

const createTask = (inputText) => {
    if (!inputText) return;
    const li = document.createElement('li');
    li.innerText = inputText;
    createADeleteButton(li);
    tasks.appendChild(li);
    saveTask();
}



const createADeleteButton = (li) => {
    li.innerText += ' ';
    const deleteButton = document.createElement('button');
    deleteButton.innerText = 'Apagar';
    deleteButton.setAttribute('class', 'delete');
    li.appendChild(deleteButton);   
}

document.addEventListener('click', function (event) {
    const element = event.target;
    if (element.classList.contains('delete')) {
        element.parentElement.remove();
        saveTask()
    }
})

const saveTask = () => {
    const liTasks = tasks.querySelectorAll('li');
    const tasksArray = [];

    for (let task of liTasks) {
        let taskText = task.innerText;
        taskText = taskText.replace('Apagar', '').trim();
        tasksArray.push(taskText);
    }

    const tasksJSON = JSON.stringify(tasksArray);
    localStorage.setItem('tasks', tasksJSON);
}

const addSavedTasks = () => {
    const tasks = localStorage.getItem('tasks');
    const tasksArray = JSON.parse(tasks);
    
    for(let task of tasksArray) {
        createTask(task);
    }
}

addSavedTasks()