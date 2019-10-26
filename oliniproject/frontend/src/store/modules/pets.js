// import router from "../../router";
import {setToken} from "../../helpers/auth-helper";
import petsService from "../../services/pets-service";

export default {
  state: {
    pets: [],
    pet: {}
  },
  mutations: {
    setPets(state, pets) {
        state.pets = pets;
    },

    setPet(state, pet) {
        state.pet = pet;
    }
  },
  actions: {
    getPets({commit}) {
        petsService.getPets()
        .then(res => {
            if(res.status === 200) {
                commit("setPets", res.data);
            }
        })
        .catch(err => console.log(err));
    },

    getPet({commit}, petId) {
        petsService.getPet(petId)
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
