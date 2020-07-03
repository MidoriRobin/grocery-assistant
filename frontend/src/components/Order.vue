<template>
  <div class="order-page">
    <h2>Your order is on its way.</h2>
    <button type="button" name="button">Track Your Order</button>
    <ul class="summary">
      <li>Order # : {{ order.orderid }}</li>
      <li>Order Date: {{ order.date_ordered }}</li>
      <li>Order Total: ${{ order.sale_value}}</li>
    </ul>
    <!-- displays all the items from your cart -->
    <div class="order-section">
      <table cellspacing=0>
        <tr>
          <th>Items Shipped</th>
          <th>Qty</th>
          <th>Price</th>
        </tr>
        <tr v-for="item in items" :key="item.id">
          <!-- use directive to display all the orders -->
          <td>{{ item.Item.item_name }}-</td>
          <td>{{item.quantity}}</td>
          <td> {{ item.Item.cost }}</td>
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
        items: '',
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
            this.items = jsonResponse.status.items;
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
ul.summary > li{
  margin-bottom: 8px;
  font-weight: bold;
}
table{
  width: 100%;
  background: white;
  height:
}

ul.summary{
  background-color: white;
}

tr{
  width: 100%;
}
</style>
