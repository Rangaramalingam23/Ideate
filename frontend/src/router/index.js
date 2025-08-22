import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../pages/LandingPage.vue'
import Login from '../pages/Login.vue'
import Signup from '../pages/Signup.vue'
import Dashboard from '../pages/Dashboard.vue'
import Messages from '../pages/Messages.vue'
import Discover from '../pages/Discover.vue'
import MainLayout from '../components/layout/MainLayout.vue'

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  // Protected routes with navigation layout
  {
    path: '/',
    component: MainLayout,
    children: [
      {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard
      },
      {
        path: '/discover',
        name: 'Discover',
        component: Discover
      },
      {
        path: '/messages',
        name: 'Messages',
        component: Messages
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router