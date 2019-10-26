import axios from "axios";
import {authHeader} from "../helpers/auth-helper";

export default {
    getPets() {
        return new Promise((resolve, reject) => {
            resolve({
                status: 200,
                data: [
                    {
                        img: "this is image",
                        id: 0,
                        status: "stat0"
                    },
                    {
                        img: "this is image1",
                        id: 1,
                        status: "stat1"
                    },
                    {
                        img: "this is image1",
                        id: 2,
                        status: "stat1"
                    },
                    {
                        img: "this is image1",
                        id: 3,
                        status: "stat1"
                    },
                    {
                        img: "this is image1",
                        id: 4,
                        status: "stat1"
                    },
                    {
                        img: "this is image1",
                        id: 5,
                        status: "stat1"
                    },
                    {
                        img: "this is image1",
                        id: 6,
                        status: "stat1"
                    }
                ]
            });
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