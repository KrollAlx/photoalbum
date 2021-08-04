import Vue from 'vue'
import VueRouter from 'vue-router'
import SignIn from '../views/SignIn'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'sign-in',
    component: SignIn
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: () => import('../views/SignUp.vue')
  },
  {
    path: '/albums',
    name: 'albums',
    component: () => import('../views/Albums.vue')
  },
  {
    path: '/album/:id',
    name: 'album',
    component: () => import('../views/AlbumDetail.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
