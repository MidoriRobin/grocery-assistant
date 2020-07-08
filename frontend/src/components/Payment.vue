<!-- this component serves to display and add functionality for payments/checkout -->
<template>
  <div class="pay-page">
    <form>
      <ul class="bill-info">
        <li><h5>Billing Info</h5></li>
        <li>
          <label for="full-name"> Full Name</label>
          <input type="text" name="full-name">
        </li>
        <li>
          <label for="address">Address</label>
          <input type="text" name="address">
        </li>
        <li>
          <label for="city">City</label>
          <input type="text" name="city">
        </li>
        <li>
          <label for="country">Country</label>
          <input type="text" name="country">
        </li>
      </ul>
      <ul class="cc-info">
        <li>Credit Card Info</li>
        <li>
          <label for="card-number">Card Number</label>
          <input type="number" name="card-number">
        </li>
        <li>
          <label for="cd-name">CardHolder Name</label>
          <input type="text" name="cd-name">
        </li>
        <li>
          <label for="expire-date">Expire Date</label>
          <input type="text" name="expire-date">
        </li>
        <li>
          <label for="ccv">CVV</label>
          <input type="number" name="ccv">
        </li>
      </ul>
      <button type="submit" name="submit">Complete Purchase</button>
    </form>
    <button @click="finishOrder">Complete Order</button>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Payment',
  data: () => ({
    message: '',
    error: '',
  }),

  methods: {
    finishOrder: function() {
      console.log("Completing order");
      let usid = sessionStorage.getItem('usid');
      let crtid = sessionStorage.getItem('crtid');
      let resp = '';

      fetch('http://localhost:5000/api/users/' + usid + '/cart/'
      + crtid + '/orders',{
        method: 'POST',
        headers: {},

      })
      .then(function (response) {
          resp = response.status;
          return response.json();
      })
      .then((jsonResponse) => {
          console.log(jsonResponse);

          if(resp === 201) {
            console.log("OK, making order");
            sessionStorage.setItem('crtid', jsonResponse.status.cartid);
            this.$router.push('/orders')

          } else {
            console.log("Not OK");
          }
      })
      .catch(function (error) {
          console.log(error);
      });
    },

    goToOrders: function() {
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

          if(resp === 201) {
            console.log("OK, making order");
            this.$router.push('/orders');
          } else {
            console.log("Not OK");
          }
      })
      .catch(function (error) {
          console.log(error);
      });
    }
  }
};
/* eslint-enable */
</script>

<style>
</style>
