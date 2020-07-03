<template>
  <div class="order-page">
    <h2>Your order is on its way.</h2>
    <button type="button" name="button">Track Your Order</button>
    <ul class="summary">
      <li>Order # : {{ order.orderid }}</li>
      <li>Order Date: {{ order.date_ordered }}</li>
      <li>Order Total: ${{ order.sale_value}}</li>
    </ul>
    <div class="summary">
      <p> </p>
      <p></p>
      <p></p>
    </div>
    <!-- displays all the items from your cart -->
    <div class="order-section">
      <table>
        <tr>
          <th>Items Shipped</th>
          <th>Qty</th>
          <th>Price</th>
        </tr>
        <tr >
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
            resp = response.status;
            return response.json();
        })
        .then((jsonResponse) => {
            console.log(jsonResponse.status);
            this.message = jsonResponse.status.message;
            this.order = jsonResponse.status.order;
        })
        .catch(function (error){
          console.log(error);
        });
      },
    },
    created: function() {
      console.log('Orders ago show now...');
      //do something after creating vue instance
      this.showOrder();
    }
  };
/* eslint-enable */
</script>
<style scoped>

ul.summary{
  background-color: white;
}

tr{
  width: 100%;
}
</style>
