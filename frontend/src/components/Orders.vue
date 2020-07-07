<template>
  <div class="orders-page">
    <div class="orders-area">
      <h2> Orders </h2>
      <ul v-if="orders != []" class="orders">
        <li v-for="order in orders" :key="order.id">
          <router-link :to="{ name: 'Order', params: { orderid: order.orderid }}">
            <h3> Order#: {{ order.orderid }} </h3>
          </router-link>
          <router-link :to="{ name: 'Order', params: { orderid: order.orderid }}">
            <h4>{{ order.date_ordered }}</h4>
          </router-link>
          <p>Items in order: {{ order.no_items }}</p>
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

div.orders-page {
  display: grid;
  grid-template-rows: 20% 80%;
  grid-template-columns: 80% 20%;
  border: 2px solid black;
  /* height: 1000px; */
  width: 70%;
  margin: 0 auto;
  margin-top: 50px;
  margin-bottom: 50px;
}

div.orders-area {
  display: grid;
  grid-column: 1 / 2;
}

ul.orders li{
  display: grid;
  grid-template-columns: 250px auto 200px;
  border-top-style: solid;
  border-top-color: blue;
  border-radius: 10px;
  box-shadow: 1px 3px 4px gray;
  padding: 10px;
  margin: 20px;
  height: 100px;
}

.orders button{
  grid-column: 3;
  margin-top: auto;
  margin-bottom: auto;
  height: 50px;
}
</style>
