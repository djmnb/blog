<template>
  <div>
    <div>
      <div>a:{{ a }} &nbsp; b:{{ b }}</div>
      <div>
        <button @click="a++">a++</button> <button @click="b++">b++</button>
      </div>
      <div>{{ c }}</div>
      <div>{{ d }}</div>
      <Test helloWorld="hhh"></Test>
    </div>
  </div>
</template>

<script setup>
import { reactive, toRefs, ref, shallowRef } from "vue";
import Test from "./components/Test.vue"


const b = 1;
const a = ref(1)
const c = reactive({
  mes: "hello"
});
const d = ref({
  mes: "hello"
});
    
   

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
