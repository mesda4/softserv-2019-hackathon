export const getToken = () => {
    return localStorage.getItem("token");
}

export const setToken = token => {
    localStorage.setItem("token", token);
}

export const authHeader = {
    "Authorization": getToken() ? "JWT " + getToken() : ""
}