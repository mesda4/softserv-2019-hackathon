// import router from "../../router";
import petService from "../../services/pets-service";
import {setToken} from "../../helpers/auth-helper";

export default {
  state: {
    pets: [
        {
            img: "this is image",
            id: 0,
            status: "stat0"
        },
        {
            img: "this is image1",
            id: 1,
            status: "stat1"
        }
    ],
    pet: {}
  },
  mutations: {
      setPet(state, pet) {
          state.pet = pet;
      }
  },
  actions: {
    getPet({commit}, id) {
        petService.getPet(id)
        .then(res => {
            if(res.status === 200) {
                commit("setPet", res.data);
            }
        })
        .catch(err => console.log(err));
    }
  }
};
