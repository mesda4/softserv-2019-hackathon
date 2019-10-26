import axios from "axios";
import {authHeader} from "../helpers/auth-helper";

export default {
    login(form) {
        return axios.post("https://hackathon.spdns.eu/auth/login/", form);
    },

    register(form) {
        return axios.post("https://hackathon.spdns.eu/auth/register/", form);
    }
}