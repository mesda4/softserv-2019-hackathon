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
  getters: {
    getRole(state) {
        return state.user.is_staff ? "stuff" : "user";
    }
  },
  actions: {
    // REQUEST TO API
    login({commit, dispatch}, form) {
        userService.login(form)
        .then(res => {
            console.log(res);
            if(res.status === 200) {
                setToken(res.data.token);
                // dispatch("getRole");
                router.push("/");
            }
        })
        .catch(err => console.log(err.response));
    },

    register({commit, dispatch}, form) {
      return new Promise((resolve, reject) => {
        userService.register(form)
        .then(res => {
            if(res.status === 200) {
                setToken(res.data.token);
                router.push("/");
                // dispatch("getRole");
                resolve();
            }
        })
        .catch(err => {
            if(err.response) {
                reject(err.response.data);
            }
        });
      });
    },

    getRole({commit}) {
        userService.getRole()
        .then(res => {
            if(res.status === 200) {
                commit("setUser", res.data);
            }
        })
        .catch(err => console.log(err));
    }

    // auth({commit}) {
    //   commit("setAuthState", true);
    // }
  }
};
