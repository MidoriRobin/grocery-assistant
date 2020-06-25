<!-- this component serves to display and add functionality for payments/checkout -->
<template>
  <div class="pay-page">
    <form>
      <ul>
        <li><h5>Billing Info</h5></li>
        <li>
          <label for="full-name"> Full Name</label>
          <input type="text" name="full-name" required>
        </li>
        <li>
          <label for="address">Address</label>
          <input type="text" name="address" required>
        </li>
        <li>
          <label for="city">City</label>
          <input type="text" name="city" required>
        </li>
        <li>
          <label for="country">Country</label>
          <input type="text" name="country" required>
        </li>
      </ul>
      <ul>
        <li>Credit Card Info</li>
        <li>
          <label for="card-number">Card Number</label>
          <input type="number" name="card-number" required>
        </li>
        <li>
          <label for="cd-name">CardHolder Name</label>
          <input type="text" name="cd-name" required>
        </li>
        <li>
          <label for="expire-date">Expire Date</label>
          <input type="date" name="expire-date" required>
        </li>
        <li>
          <label for="ccv">CVV</label>
          <input type="number" name="ccv" required>
        </li>
      </ul>
      <button type="submit" name="submit">Complete Purchase</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Payment',
  data: () => ({
    message: '',
    error: '',
  }),
};
</script>

<style>
</style>
