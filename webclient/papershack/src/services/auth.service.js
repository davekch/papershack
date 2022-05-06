import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api";


// service to fetch and manage jwt tokens
class AuthService {
    login(credentials) {
        return axios
            .post(API_URL + "/token/", {
                username: credentials.username,
                password: credentials.password
            })
            .then(response => {
                if (response.data.access) {
                    localStorage.setItem("jwttoken", JSON.stringify(response.data));
                }
                return response.data;
            });
    }
    logout() {
        localStorage.removeItem("jwttoken");
    }
}


export default new AuthService();
