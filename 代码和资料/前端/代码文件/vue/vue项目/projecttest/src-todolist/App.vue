<template>
  <div class="todo-container">
    <div class="todo-wrap">
      <Myheader :todolist="todolist"></Myheader>
      <Mymain :todolist="todolist" :deletetodo="deletetodo"></Mymain>
      <Myfooter :done="done" :all="todolist.length" :removealldone="removealldone"></Myfooter>
    </div>
  </div>
</template>

<script>
import Myfooter from "./components/footer.vue";
import Myheader from "./components/header.vue";
import Mymain from "./components/main.vue";
import { nanoid } from "nanoid";
export default {
  name: "App",
  components: {
    Myfooter,
    Myheader,
    Mymain,
  },
  data() {
    return {
      todolist: [{ id: nanoid(), status: false, todo: "吃饭" }],
    };
  },
  methods: {
    deletetodo(id) {
      this.todolist = this.todolist.filter((obj) => obj.id != id);
    },
    removealldone() {
      this.todolist = this.todolist.filter((obj) => !obj.status)
    }
  },
  computed: {
    done() {
      return this.todolist.filter((obj) => obj.status).length
    }
  }
};
</script>

<style>
/*base*/
body {
  background: #fff;
}

.btn {
  display: inline-block;
  padding: 4px 12px;
  margin-bottom: 0;
  font-size: 14px;
  line-height: 20px;
  text-align: center;
  vertical-align: middle;
  cursor: pointer;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2),
    0 1px 2px rgba(0, 0, 0, 0.05);
  border-radius: 4px;
}

.btn-danger {
  color: #fff;
  background-color: #da4f49;
  border: 1px solid #bd362f;
}

.btn-danger:hover {
  color: #fff;
  background-color: #bd362f;
}

.btn:focus {
  outline: none;
}

.todo-container {
  width: 600px;
  margin: 0 auto;
}
.todo-container .todo-wrap {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

/*header*/
.todo-header input {
  width: 560px;
  height: 28px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 4px 7px;
}

.todo-header input:focus {
  outline: none;
  border-color: rgba(82, 168, 236, 0.8);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075),
    0 0 8px rgba(82, 168, 236, 0.6);
}
</style>
