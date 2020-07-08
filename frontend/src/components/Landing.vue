<template>
<div class="landing">
  <div class="cta">
    <h1>Welcome to Quikshop!</h1>
    <p>Food is a very important part of our lives, so why hassle to get it?
    Here at Quikshop we have decided to bring the grocery store to you.
    You can shop from the comfort of your home and even while on the go!</p>
       <!-- <About/> -->
    <button @click="goShopping" type="button" name="shop-now">Shop Now</button>
  </div>
</div>
</template>

<script>
/* eslint-disable */
import About from '@/views/About.vue';
import Navigation from '@/components/Navigation.vue'

export default {
  name: 'Landing',
  components: {
    About,
    Navigation
  },
methods:{
  goShopping: function(){
    console.log('Heading back to the shopping page...');
    this.$router.push('/items')
  }
}
};

/* eslint-enable */
</script>

<style scoped>

html,body{
  height:100%;
  margin: 0;
  font: Arial;
}

.landing{
  background-image: url("background2.jpg");
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  overflow: auto;
}

.cta{
  background-color: #CCCCFF;
  width: 60%;
  margin-top: 10%;
  margin-left: auto;
  margin-right: auto;
  background-color: white;
  border: 1px solid black;
  padding: 30px 30px;
}

.cta > p{
  font-size: 20px;
  line-height: 30px;
}

div.cta > button{
  background-color: #4CAF50;
  border: none;
  color: white;
  text-align: center;
  height: 80px;
  width: 250px;
  border-radius: 8px;
  font-size: 20px;
  margin-top: 10px;
}

div.cta > button:hover{
  background-color: white;
  border: 3px solid #4CAF50;
  color: #4CAF50;
}
</style>
