<template>
  <div id="app">
    <ul class="top-first">
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/about">About</router-link></li>
      <li><router-link to="/ping">Ping</router-link></li>
      <li><router-link to="/login">Login</router-link></li>
      <li><router-link to="/test">Test</router-link></li>
      <li><router-link to="/landing">Landing</router-link></li>
    </ul>
    <router-view/>
  </div>
</template>

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
/* ul.top-second > li{
  display:grid;
  float: left;
} */
</style>
