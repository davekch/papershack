import AuthService from '../services/auth.service';

const token = JSON.parse(localStorage.getItem("jwttoken"));
const initialState = token
    ? { status: { loggedIn: true }, token: token }
    : { status: { loggedIn: false }, token: null };


// this object is going to be placed in a vuex store
export const auth = {
    namespaced: true,
    state: initialState,
    actions: {
        login({ commit }, credentials) {
            return AuthService.login(credentials).then(
                token => {
                    commit('loginSuccess', token);
                    return Promise.resolve(token);
                },
                error => {
                    commit('loginFailure');
                    return Promise.reject(error);
                }
            );
        },
        logout({ commit }) {
            AuthService.logout();
            commit('logout');
        },
    },
    mutations: {
        loginSuccess(state, token) {
            state.status.loggedIn = true;
            state.token = token;
        },
        loginFailure(state) {
            state.status.loggedIn = false;
            state.token = null;
        },
        logout(state) {
            state.status.loggedIn = false;
            state.user = null;
        }
    }
};
