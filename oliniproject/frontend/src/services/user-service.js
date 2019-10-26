import axios from "axios";
import {authHeader} from "../helpers/auth-helper";

const getToken = () => {
    return localStorage.getItem("token");
}

export default {
    login(form) {
        return axios.post("https://hackathon.spdns.eu/auth/login/", form);
    },

    register(form) {
        return axios.post("https://hackathon.spdns.eu/auth/register/", form);
    },

    getUser() {
        return axios.get("https://hackathon.spdns.eu/auth/info/", {
            headers: {
                "Authorization": getToken() ? "JWT " + getToken() : ""
            }
        });
    }
}