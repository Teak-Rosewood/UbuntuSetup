/*
  Implement a class `Todo` having below methods
    - add(todo): adds todo to list of todos
    - remove(indexOfTodo): remove todo from list of todos
    - update(index, updatedTodo): update todo at given index
    - getAll: returns all todos
    - get(indexOfTodo): returns todo at given index
    - clear: deletes all todos

  Once you've implemented the logic, test your code by running
*/

class Todo {
  constructor(){
    this.list = [];
  }

  add (todo){
    this.list.push(todo);
  }

  remove(indexOfTodo){
    if(indexOfTodo < this.list.length){
      this.list.remove(indexOfTodo);
    }
  }
  
  update (index, updatedTodo){
    if(indexOfTodo < this.list.length){
      this.list[index] = updatedTodo;
    }
  }
  getAll(){
    return this.list;
  }
  get(indexOfTodo){
    if(indexOfTodo < this.list.length){
      return this.list[indexOfTodo];
    }
    else {
      return null;
    }
  }
  clear(){
    this.list.clear();
  }
}

module.exports = Todo;
