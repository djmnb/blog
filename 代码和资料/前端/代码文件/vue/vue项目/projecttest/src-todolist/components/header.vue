<template>
  <div class="todo-header">
    <input type="text" placeholder="请输入你的任务名称，按回车键确认" v-model="todo" @keydown.enter="addtodo"/>
  </div>
</template>

<script>
import {nanoid} from "nanoid";
export default {
    data() {
        return {
            todo:""
        
        };
    },
    props: ["todolist"],
    methods: {

        addtodo(){
            this.todolist.push({id:nanoid(), status: false, todo: this.todo })
            this.todo = ""
        },
    
    },
    mounted() {
        console.log(this)
    }
};
</script>

<style>
</style>