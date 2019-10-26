import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex)

import auth from "./modules/auth";
import pets from "./modules/pets";

export default new Vuex.Store({
  modules: {
    auth,
    pets
  },
  state: {
  },
  mutations: {
  },
  actions: {
  }
})
