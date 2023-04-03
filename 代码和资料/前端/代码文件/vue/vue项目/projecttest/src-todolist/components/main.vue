<template>
  <ul class="todo-main">
    <li v-for="todo in todolist" :key="todo.id">
      <label>
        <input type="checkbox" v-model="todo.status"/>
        <span>{{ todo.todo }}</span>
      </label>
      <button class="btn btn-danger" @click="deletetodo(todo.id)">删除</button>
    </li>
  </ul>
</template>

<script>
export default {
    props: ["todolist","deletetodo"],
    
};
</script>

<style scoped>
/*main*/
.todo-main {
  margin-left: 0px;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0px;
}

.todo-empty {
  height: 40px;
  line-height: 40px;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding-left: 5px;
  margin-top: 10px;
}
/*item*/
li {
  list-style: none;
  height: 36px;
  line-height: 36px;
  padding: 0 5px;
  border-bottom: 1px solid #ddd;
}

li label {
  float: left;
  cursor: pointer;
}

li label li input {
  vertical-align: middle;
  margin-right: 6px;
  position: relative;
  top: -1px;
}

li button {
  float: right;
  display: none;
  margin-top: 3px;
}

li:before {
  content: initial;
}

li:last-child {
  border-bottom: none;
}


ul li .btn{
    display: none;
}

ul li:hover .btn{
    display: block;
}
</style>