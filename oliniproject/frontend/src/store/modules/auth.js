// import userService from "../../services/user-service";
// import router from "../../router";

// const token = localStorage.getItem("token");
// let isAuthenticated = token ? true : false;

export default {
  state: {
    // isAuthenticated,
    // user: {}
  },
  mutations: {
    // setAuthState(state, cond) {
    //   state.isAuthenticated = cond;
    //   if(!cond) state.user = null;
    // },

    // setUser(state, userData) {
    //   state.user = userData;
    // }
  },
  actions: {
    // REQUEST TO API
    login() {
        console.log(11);
    //   userService.login(form)
    //   .then(userData => {
    //       commit("setUser", userData);
    //       commit("setAuthState", true);
    //       router.push("personalCabinet");
    //     });
    },

    // register({commit}, form) {
    //   userService.register(form)
    //     .then(userData => {
    //       commit("setUser", userData);
    //       commit("setAuthState", true);
    //     });
    // },

    // auth({commit}) {
    //   commit("setAuthState", true);
    // }
  }
};
