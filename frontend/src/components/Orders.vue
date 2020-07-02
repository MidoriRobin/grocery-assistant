<template>
  <div class="orders-page">
    <ul v-if="orders === []">
      <li v-for="order in orders" :key="order.id">
        <router-link :to="{ name: 'Order', params: { orderid: order.order_id }}">
          <h4>{{ order.date_ordered }}</h4>
        </router-link>
        <p>{{ order.no_items }}</p>
      </li>
    </ul>
    <ul v-else>
      <li><h3> No orders have been made yet </h3></li>
      <li>
        <p> Head to
          <button @click="goToCart">Your Cart</button>
          to checkout an order </p>
      </li>
      <li>
        <p> Or Check out
          <router-link to="/lists">Your lists</router-link> or
          <router-link to="/items">Some of our items</router-link>
          to start adding stuff to your cart
        </p>
      </li>
    </ul>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Orders',
  data() {
    return {
      message: '',
      error: '',
      orders: [],
    };
  },

  methods: {
    getOrders: function() {
      console.log("Viewing orders");
      let usid = sessionStorage.getItem('usid');
      let crtid = sessionStorage.getItem('crtid');
      let resp = '';

      fetch('http://localhost:5000/api/users/' + usid + '/orders/',{
        method: 'GET',
        headers: {},

      })
      .then(function (response) {
          resp = response.status;
          return response.json();
      })
      .then((jsonResponse) => {
          console.log(jsonResponse);
          this.orders = jsonResponse.status.orders
      })
      .catch(function (error) {
          console.log(error);
      });
    },
    goToCart: function() {
        console.log("Navigating to cart..");
        // let meid = sessionStorage.getItem('usid');
        let usid = sessionStorage.getItem('usid');
        this.$router.push('/users/' + usid + '/cart');
    },
  },
  created: function() {
    console.log("entered the order page");
    this.getOrders();
  }
};
/* eslint-enable */
</script>

<style>
</style>
