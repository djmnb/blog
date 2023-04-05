import Vue from 'vue'
import App from './App.vue'

// 关闭生产提示
Vue.config.productionTip = false
import VueRouter from 'vue-router'
Vue.use(VueRouter)

import router from './router'

let vm = new Vue({
  router,
  // 渲染页面
  render: h => h(App),
  mounted() {
    console.log(this)
  }
}).$mount('#root')   //挂在到id为root的容器中
