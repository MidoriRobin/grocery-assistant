<template>
<div class="landing">
  <Navigation/>
  <div class="cta">
    <h1>Welcome to Quikshop!</h1>
    <p>Sed laoreet urna dolor, ut feugiat ipsum tempor ac.
      Nullam a elonec volutpat tellus gravida sem placerat,
      sed pharetra nisi consequat. Etiam suscipit orci eu nulla ultricies semper.
       Donec dignissim enim id velit egestas, sed aliquet lorem luctus.</p>
       <!-- <About/> -->
    <button type="button" name="shop-now">Shop Now</button>
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
  width: 50%;
  margin-top: 10%;
  margin-left: auto;
  margin-right: auto;
  background-color: white;
  border: 2px solid black;
  padding: 30px 30px;
}

div.cta > button{
  background-color: #4CAF50;
  border: none;
  color: white;
  text-align: center;
  height: 80px;
  width: 200px;
  border-radius: 8px;
}

div.cta > button:hover{
  background-color: white;
  border: 3px solid #4CAF50;
  color: #4CAF50;
}
</style>
