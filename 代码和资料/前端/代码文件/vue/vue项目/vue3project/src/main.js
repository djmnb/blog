import { createApp,ref } from 'vue'
import App from './App.vue'

let app = createApp(App).mount('#app')
window.test = app
window.ref = ref


