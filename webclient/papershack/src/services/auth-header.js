// helper function to get the authorization header
export default function authHeader() {
    let token = JSON.parse(localStorage.getItem("jwttoken"));
    if (token && token.access) {
        return { Authorization: "Bearer " + token.access };
    } else {
        return {};
    }
}
