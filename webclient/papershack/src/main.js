import { createApp } from 'vue'
import App from './App.vue'
import { createStore } from "vuex";
import { createRouter, createWebHashHistory } from 'vue-router';
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

// create a store to hold the jwt token
const store = createStore({
    state() {
        return {
            tokenAccess: null,
            tokenRefresh: null,
        };
    },
    mutations: {
        setTokenAccess(state, access) {
            state.tokenAccess = access;
        },
        setTokenRefresh(state, refresh) {
            state.tokenRefresh = refresh;
        },
    },
    actions: {},
    getters: {
        isAuthenticated(state) {
            return !!state.tokenAccess;
        },
        getTokenAccess(state) {
            return state.tokenAccess;
        },
        getTokenRefresh(state) {
            return state.tokenRefresh;
        },
    },
});

const app = createApp(App)
app.use(store)
app.use(router)
app.mount('#app')
