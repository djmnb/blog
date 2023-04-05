<template>
  <div>
    <div>
     <div> a:{{ a }} &nbsp; b:{{ b }}</div>
     <div> <button @click="a++">a++</button> <button @click="b++">b++</button></div>
     <div>{{ c }}</div>
     <div>{{ d }}</div>
    </div>
  </div>
</template>

<script>
import { reactive, toRefs, ref, shallowRef } from "vue";

export default {
  name: "App",
  components: {},
  setup() {
    let t = {
      b:1,
      a: ref(1),
      c: reactive({
        mes:"hello"
      }),
      d: ref({
        mes:"hello"
      })
    };
    window.t = t
    return t;
  }
   

};
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
