export const getToken = () => {
    return localStorage.getItem("token");
}

export const authHeader = {
    "Authorization": getToken() ? "Bearer " + getToken().access_token : ""
}