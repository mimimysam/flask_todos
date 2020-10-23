let todoForm = document.querySelector("#todo-form");

let todoCountSpan = document.querySelector("#todo-count");

function countTodos(){
    var todoList = document.getElementById("todo-list").getElementsByTagName("li");
    todoCountSpan.innerHTML = todoList.length;
}

countTodos()

