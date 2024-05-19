import './assets/main.css'
import './assets/fonts.css'
import '@fortawesome/fontawesome-free/css/all.css'
import router from './router/index.js';

import { createApp } from 'vue'
import App from './App.vue'

createApp(App)
.use(router)
.mount('#app')
