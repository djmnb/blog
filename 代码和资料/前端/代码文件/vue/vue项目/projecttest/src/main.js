import Vue from 'vue'
import App from './App.vue'
import vuex from "vuex"
import store from "./store/index"

// 关闭生产提示
Vue.config.productionTip = false



let vm = new Vue({

  store,
  // 渲染页面
  render: h => h(App),
  mounted() {
    console.log(this)
  }
}).$mount('#root')   //挂在到id为root的容器中
