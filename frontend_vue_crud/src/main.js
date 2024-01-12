import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './style.css'

// createApp(App).use(router).mount('#app')

const app = createApp(App)

app.use(router)

app.mount('#app')

