<template>
  <div id="app">
    <ul class="top-first">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/about">About</router-link></li>
      <li><router-link to="/ping">Ping</router-link></li>
      <li><router-link to="/login">Login</router-link></li>
      <li><router-link to="/signup">Signup</router-link></li>
      <li><router-link to="/landing">Landing</router-link></li>
      <li><router-link to="/lists">Shopping List</router-link></li>
      <li v-if="show"><button id="navi" @click="logout">Logout</button></li>
    </ul>
    <router-view/>
  </div>
</template>

<script>
/* eslint-disable */

export default {
  name: "",
  data: () => ({
    message: '',
    error: '',
    show: true,
  }),

  watch: {
    ifLogged: function() {
      if(!sessionStorage.getItem('usid')) {
        show = false;
      } else {
        show = true;
      }
    }
  },

  methods: {
    logout: function() {
      console.log("logging out user..")
      sessionStorage.clear()

      fetch('http://localhost:5000/api/logout', {
          method: 'GET',
          headers: {},
      })
      .then(function (response){
          // resp = response.status;
          console.log(response);
          return response.json();
      })
      .then((jsonResponse) => {
          this.message = jsonResponse.status.message;
          this.$router.push('/');
          console.log(jsonResponse);
      })
      .catch(function (error) {
          console.log(error);
      });

    },
  }
}

/* eslint-enable */
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color:#90ee90;
}

ul.top-first > li{
   float: left;
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

ul.top-first > h1{
  font-size: 20px;
  display: inline;
  float: left;
  padding-left: 10px;
}

button#navi {
  background: none;
  color: black;
  border-radius: 0;
  border: none;
  margin: 0;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 15px;
  padding-right: 15px;
  font: inherit;
  outline: inherit;
}

button#navi:hover {
  color: white;
  background-color: #111;
}

/* ul.top-second > li{
  display:grid;
  float: left;
} */
</style>
