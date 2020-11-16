import Vue from 'vue'
import VueRouter from 'vue-router'

// import store from '@/store'
Vue.use(VueRouter)

const routes = [{
  path: '/',
  name: 'Home',
  component: () =>
    import('../views/Home.vue'),
  meta: { title: 'Shopping Site' }
}]

const router = new VueRouter({
  // mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title

  next()
})

export default router
