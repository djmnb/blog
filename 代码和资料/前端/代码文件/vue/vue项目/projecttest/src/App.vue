<template>
  <div>
    {{ test }}
      <button @click="change">修改</button>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {},
  data() {
    let t = {
      test: {
        b:"fsdfds"
      }
    }
    console.log(t)
    return t
  },
  methods: {
    change() {
      let t = {
        a:'111'
      }
      console.log("aaa",t)
      this.test = t
      
    }
  }
};
</script>

<style>
</style>
