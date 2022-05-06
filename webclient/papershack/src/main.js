import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHashHistory } from 'vue-router';
import store from "./store"
import RecordsList from "./components/RecordsList.vue";
import LogIn from "./components/LogIn.vue";


const routes = [
    { path: "/", component: LogIn },
    { path: "/records", component: RecordsList },
    { path: "/login", component: LogIn },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
})

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')
