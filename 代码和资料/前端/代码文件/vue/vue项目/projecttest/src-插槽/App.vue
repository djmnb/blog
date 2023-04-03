<template>
  <div>
    <test>
      
      <h1>{{ message }}</h1>
     
    </test>
  </div>
</template>

<script>
import test from './components/test.vue';

export default {
  name: 'APP',
  components: {
    test
  },
  data() {
    return {
      message:"hello"
    }
  }
}
</script>

<style>
</style>
