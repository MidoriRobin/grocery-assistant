<template>
  <div >
    <!-- <p>Hello {{ name }}. This is the landing page</p> -->
    <div class="top-nav">
      <h1 class="logo left">LOGO</h1>
      <input type="text" placeholder="Search...">
      <a href="#">Login</a>
      <a href="#">Signup</a>
    </div>
    <div class="second-nav">

    </div>
  </div>
</template>

<script>
export default {
  name: 'Landing',
  data() {
    return {
      name: 'Giselle',
    };
  },
};
</script>

<style>
  a {
    padding-right: 5px;
  }
</style>
