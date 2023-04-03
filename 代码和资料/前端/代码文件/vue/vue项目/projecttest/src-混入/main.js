import Vue from 'vue'
import App from './App.vue'

// 关闭生产提示
Vue.config.productionTip = false


Vue.mixin({
  data() {
    return {
      a: 10,
      b: 20,
    }
  }
})

let vm = new Vue({
  // 渲染页面
  render: h => h(App),
}).$mount('#app')   //挂在到id为app的容器中
