import router from "../../router";
import userService from "../../services/user-service";
import {setToken} from "../../helpers/auth-helper";

// const token = localStorage.getItem("token");
// let isAuthenticated = token ? true : false;

export default {
  state: {
    // isAuthenticated,
    user: {}
  },
  mutations: {
    // setAuthState(state, cond) {
    //   state.isAuthenticated = cond;
    //   if(!cond) state.user = null;
    // },

    setUser(state, userData) {
      state.user = userData;
    }
  },
  actions: {
    // REQUEST TO API
    login({commit}, form) {
        userService.login(form)
        .then(res => {
            console.log(res);
            if(res.status === 200) {
                const userData = {
                    email: res.data.name
                };
                commit("setUser", userData);

                setToken(res.data.token);
                router.push("home");
            }
        })
        .catch(err => {
            console.log(err.response);
        });
    },

    register({commit}, form) {
      userService.register(form)
        .then(userData => {
            console.log(userData);
        //   commit("setUser", userData);
        //   commit("setAuthState", true);
        });
    },

    // auth({commit}) {
    //   commit("setAuthState", true);
    // }
  }
};
