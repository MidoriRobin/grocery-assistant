import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Ping from '../components/Ping.vue';
import Login from '../components/Login.vue';
import Test from '../components/Test.vue';
import SingleItem from '../components/SingleItem.vue';
import ShoppingCart from '../components/ShoppingCart.vue';
import Payment from '../components/Payment.vue';
import Items from '../components/Items.vue';
import Landing from '../components/Landing.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/test',
    name: 'Test',
    component: Test,
  },
  {
    path: '/items/:itemid',
    name: 'SingleItem',
    component: SingleItem,
  },
  {
    path: '/users/:userid/cart',
    name: 'ShoppingCart',
    component: ShoppingCart,
  },
  {
    path: '/payment',
    name: 'Payment',
    component: Payment,
  },
  {
    path: '/items',
    name: 'Items',
    component: Items,
  },
  {
    path: '/landing',
    name: 'Landing',
    component: Landing,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
