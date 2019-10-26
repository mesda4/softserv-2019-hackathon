import Vue from "vue"
import VueRouter from "vue-router"

import {getToken} from "../helpers/auth-helper";

import Home from "../views/Home.vue"
import Needs from "../modules/needs/Table.vue"
Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
    children: 
    [
      {
      path: 'needs',
      component: Needs
      },
    ]
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
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const {permissions} = to.meta;

  if(permissions) {
    console.log(permissions);
    console.log(permissions.find(role => role !== "guest"));
  }
  // if(permissions.find(role => role !== "guest"))

  // const token = getToken();
  // if(token) {

  // }
  next();
});

export default router
