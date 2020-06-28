<template>
  <div class="flash-area">
    <h4 class="error" v-if="error">{{error}}</h4>
    <h4 class="message" v-if="message">{{message}}</h4>
  </div>
</template>

<script>
/* eslint-disable*/
export default {
  name: 'Flash',
  props: {
    error: String,
    message: String
  },

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

<style>

div.flash-area {
  height: 25px;
  width:inherit;
  text-align: center;
  margin: 0 auto;
}

div.flash-area > .error {
  background-color: #CC7178;
}

div.flash-area > .message {
    background-color: #009F6B;
    color: white;
}

</style>
