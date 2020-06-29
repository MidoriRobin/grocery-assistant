<template>
  <div id="app">
    <ul class="top-first">
      <h1>LOGO</h1>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/about">About</router-link></li>
      <li><router-link to="/ping">Ping</router-link></li>
      <li><router-link to="/login">Login</router-link></li>
      <li><router-link to="/signup">Signup</router-link></li>
      <div class="dropdown">
        <!-- <li><a>Menu</a></li> -->
        <button class="dropbtn">Menu</button>
        <!-- <a class="dropbtn">Menu <i class="fa fa-caret-down"></i></a> -->
        <div class="dropdown-content">
          <a href="#">Aisle 1<p>-Meat and Animal Products</p></a>
          <a href="#">Aisle 2</a>
          <a href="#">Aisle 3</a>
        </div>
      </div>
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
.dropbtn{
  display:inline;
}

.dropdown-content{
  position:relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #ddd;}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {display: block;}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {background-color: #3e8e41;}

.dropdown-content p{
  display: inline-block;
}

ul {
  height: 50px;
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color:#90ee90;
  /* float: right; */
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
