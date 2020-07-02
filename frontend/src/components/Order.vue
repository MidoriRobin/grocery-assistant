<template>
  <div class="order-page">
    <h2>Your order is on its way.</h2>
    <button type="button" name="button">Track Your Order</button>
    <div class="summary">
      <p>Order # : {{ order.orderid }} </p>
      <p>Order Date: {{ order.date_ordered }}</p>
      <p>Order Total: ${{ order.sale_value}}</p>
    </div>
    <!-- displays all the items from your cart -->
    <div class="order-section">
      <table>
        <tr>
          <th>Items Shipped</th>
          <th>Qty</th>
          <th></th>
        </tr>
        <tr>
          <!-- use directive to display all the orders -->
        </tr>
      </table>

    </div>
  </div>
</template>

<script>
/* eslint-disable */
  export default {
    name: 'Order',
    data() {
      return {
        order: '',
        message: '',
        errors: '',
      };
    },

    methods: {
      showOrder: function(){
        console.log('Showing order...')
        let resp = '';
        let usid = sessionStorage.getItem("usid");

        fetch('http://localhost:5000/api/users/' + usid + '/orders/' +
        this.$route.params.orderid, {
          method: 'GET',
          headers: {},
        })
        .then(function (response){
            resp = respone.status;
            return response.json();
        })
        .then((jsonResponse) => {
            console.log(jsonResponse.status.message);
            this.message = jsonResponse.status.message;
            this.order = jsonResponse.status.orders;
        })
        .catch(function (error){
          console.log(error);
        });
      },
    }
  };
/* eslint-enable */
</script>

<style>
</style>
