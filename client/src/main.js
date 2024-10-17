import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
import './styles.css'
import axios from 'axios'

const app = createApp(App)

// Vuejs router
app.use(router)

// global variables
const axiosInstance = axios.create({
  baseURL: 'http://server:5000'
  // baseURL: 'https://get.geojs.io/v1/ip'
})
app.provide('axios', axiosInstance)

// mount app to index.html
app.mount('#app')
