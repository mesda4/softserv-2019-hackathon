import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";

import { getToken } from "../helpers/auth-helper";

import Home from "../views/Home.vue";
import Needs from "../modules/needs/Table.vue";
import Contacts from "../views/Contacts.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
    children: [
      {
        path: "",
        component: () => import("../modules/pets/Pets")
      },
      {
        path: "needs",
        component: Needs
      },
      {
        path: "contacts",
        component: Contacts
      },
      {
        path: "pets/:id",
        name: "pet",
        component: () => import("../views/Pet.vue"),
        permissions: ["user", "stuff"]
      }
    ],
    meta: {
      permissions: ["guest", "user", "stuff"]
    }
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue"),
    meta: {
      mode: "log in",
      permissions: ["guest"]
    }
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../views/Login.vue"),
    meta: {
      mode: "sign up",
      permissions: ["guest"]
    }
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  const { permissions } = to.meta;

  if (permissions) {
    const token = getToken();
    let role = "guest";

    if (token) {
      if (to.path === "/login" || to.path === "/register") {
        return next({ path: "/" });
      }

      role = store.getters.getRole;
      const hasPermission = permissions.includes(role);

      if (!hasPermission) {
        return next({ path: "/" });
      }
    } else {
      if (!permissions.includes(role)) {
        if (to.path !== "/login" && to.path !== "/register") {
          return next({ path: "/login" });
        }
      }
    }
  }

  next();
});

export default router;
