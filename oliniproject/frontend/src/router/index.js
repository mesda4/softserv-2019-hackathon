import Vue from "vue"
import VueRouter from "vue-router"
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
      mode: "log in"
    }
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../views/Login.vue"),
    meta: {
      mode: "sign up"
    }
  }
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router
