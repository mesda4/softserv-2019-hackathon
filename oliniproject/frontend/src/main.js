import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

// VUELIDATE
import Vuelidate from "vuelidate";
Vue.use(Vuelidate);


// MATERIALIZE
import "materialize-css/dist/js/materialize.min";

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
