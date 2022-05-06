import axios from 'axios';
import authHeader from './auth-header';

const API_URL = "http://127.0.0.1:8000/api";


class UserService {
    getRecords() {
        return axios.get(API_URL + "/records", { headers: authHeader() });
    }
}

export default new UserService();
