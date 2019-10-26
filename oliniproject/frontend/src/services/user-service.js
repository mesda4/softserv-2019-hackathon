import axios from "axios";
import {authHeader} from "../helpers/auth-helper";

export default {
    login(form) {
        return axios.post("http://hachathon.spdns.eu:13309/auth/login", form, {
            headers: {
                ...authHeader
            }
        });
    }
}