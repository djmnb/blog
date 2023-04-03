import Vue from 'vue'
import App from './App.vue'

// 关闭生产提示
Vue.config.productionTip = false



let vm = new Vue({
  // 渲染页面
  render: h => h(App),
}).$mount('#root')   //挂在到id为root的容器中
