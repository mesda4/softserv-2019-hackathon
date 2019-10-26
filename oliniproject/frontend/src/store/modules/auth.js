import router from "../../router";
import userService from "../../services/user-service";
import {setToken} from "../../helpers/auth-helper";

export default {
  state: {
    user: {}
  },
  mutations: {
    setUser(state, userData) {
      state.user = userData;
    }
  },
  getters: {
    getRole(state) {
        if(Object.keys(state.user).length) {
            return state.user.is_staff ? "stuff" : "user";
        }
        return "guest";
    }
  },
  actions: {
    // REQUEST TO API
    login({commit, dispatch}, form) {
        userService.login(form)
        .then(res => {
            if(res.status === 200) {
                setToken(res.data.token);
                dispatch("getUser");
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
                dispatch("getUser");
                router.push("/");
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

    getUser({commit}) {
        userService.getUser()
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
