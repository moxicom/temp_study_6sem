let tasks = [];

const addTask = (taskText) => {
    return [...tasks, { text: taskText, completed: false }];
};

const toggleTaskStatus = (index) => {
    return tasks.map((task, i) => i === index ? { ...task, completed: !task.completed } : task);
};

const deleteTask = (index) => {
    return tasks.filter((task, i) => i !== index);
};

const filterTasks = (status) => {
    if (status === 'completed') {
        return tasks.filter(task => task.completed);
    } else if (status === 'pending') {
        return tasks.filter(task => !task.completed);
    }
    return tasks;
};

const renderTasks = (filteredTasks) => {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';
    filteredTasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span style="text-decoration: ${task.completed ? 'line-through' : 'none'}">${task.text}</span>
            <button onclick="toggleTask(${index})">Выполнить</button>
            <button onclick="removeTask(${index})">Удалить</button>
        `;
        taskList.appendChild(li);
    });
};

const addTaskHandler = () => {
    const taskInput = document.getElementById('task-input');
    if (taskInput.value.trim()) {
        tasks = addTask(taskInput.value.trim());
        taskInput.value = '';
        renderTasks(tasks);
    }
};

const toggleTask = (index) => {
    tasks = toggleTaskStatus(index);
    renderTasks(tasks);
};

const removeTask = (index) => {
    tasks = deleteTask(index);
    renderTasks(tasks);
};

const filterHandler = (status) => {
    const filteredTasks = filterTasks(status);
    renderTasks(filteredTasks);
};

document.getElementById('add-task').addEventListener('click', addTaskHandler);
document.getElementById('filter-all').addEventListener('click', () => filterHandler('all'));
document.getElementById('filter-completed').addEventListener('click', () => filterHandler('completed'));
document.getElementById('filter-pending').addEventListener('click', () => filterHandler('pending'));

renderTasks(tasks);
