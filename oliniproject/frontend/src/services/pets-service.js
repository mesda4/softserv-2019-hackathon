import axios from "axios";
import {authHeader} from "../helpers/auth-helper";

const getToken = () => {
    return localStorage.getItem("token");
}

export default {
    getPets() {
        // return axios.get("https://hackathon.spdns.eu/animal/list/", {
        //     headers: {
        //         "Authorization": getToken() ? "JWT " + getToken() : ""
        //     }
        // });
        return new Promise((resolve, reject) => {
            resolve({
                status: 200,
                data: [
                    {
                        id: 0,
                        status: "В поиске"
                    },
                    {
                        id: 1,
                        status: "В поиске"
                    }
                ]
            })
        });
    },

    createPet(form) {
        return axios.post("https://hackathon.spdns.eu/animal/list1/", form, {
            headers: {
                "Authorization": getToken() ? "JWT " + getToken() : ""
            }
        });
    },

    getPet(id) {
        // return axios.get("url?id=" + id, {
        //     headers: {
        //         ...authHeader
        //     }
        // });
        return new Promise((resolve, reject) => {
            resolve({
                status: 200,
                data: {
                    img: "../assets/1/1.1.jpg",
                    imgs: [

                    ],
                    id,
                    status: "stat1",
                    name: "name of pet",
                    breed: "breeed",
                    desc: "description"
                }
            });
        });
    },

    addPet() {
        //TO DO
    }
}