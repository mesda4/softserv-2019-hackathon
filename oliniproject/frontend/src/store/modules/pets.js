// import router from "../../router";
import petService from "../../services/pets-service";
import {setToken} from "../../helpers/auth-helper";
import petsService from "../../services/pets-service";

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
    getPet({commit}, petId) {
        petService.getPet(petId)
        .then(res => {
            if(res.status === 200) {
                commit("setPet", res.data);
            }
        })
        .catch(err => console.log(err));
    },

    addPet({commit}, petId) {
        petsService.addPet(petId)
        .then(res => {
            if(res.status === 200) {
                // res.data
            }
        })
        .catch(err => console.log(err));
    }
  }
};
