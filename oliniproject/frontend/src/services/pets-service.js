import axios from "axios";
import {authHeader} from "../helpers/auth-helper";

export default {
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
    }
}