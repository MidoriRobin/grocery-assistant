<template>
    <ul class="top-first">
      <a class="heading" @click="goHome"><h1>LOGO</h1></a>

      <!-- <li><a href="#"></a></li> -->
      <li><a href="#">Login</a></li>
      <li><a href="#">Signup</a></li>
      <li><a href="#">Contact Us</a></li>
    </ul>
</template>

<script>
/* eslint-disable*/
export default {
  name: 'Navigation',
  data() {
    return {};
  },

  methods: {
    goHome: function(){
      console.log("Going home");
      this.$router.push('/');
    },
  },
};

/* eslint-enable */
</script>

};

<style scoped>

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color:#90ee90;
}

ul.top-first > li{
   float: right;
 }

 li a {
   display: block;
   color: black;
   text-align: center;
   padding: 14px 16px;
   text-decoration: none;
 }
 li a:hover{
   color: white;
   background-color: #111;
 }

ul.top-first a.heading > h1{
  font-size: 20px;
  display: inline;
  float: left;
  padding-left: 10px;
}
/* ul.top-second > li{
  display:grid;
  float: left;
} */

</style>
