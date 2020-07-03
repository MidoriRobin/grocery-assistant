<template>
  <div class="login-form">
    <Flash :message="message"/>
    <Flash :error="error"/>
    <h2>Log in</h2>
    <p>Enter your login credentials</p>
    <hr>
    <form class="form-login" @submit.prevent="LoginUser" id="loginForm" method="post">
      <div class="form-group">
        <label for="username" class="sr-only">Username</label>
        <input type="text" id="username" name="username" class="form-control"
        placeholder="Your username" required>
      </div>
      <div class="form-group">
        <label for="password" class="sr-only">Password</label>
        <input type="password" id="password" name="password" class="form-control"
        placeholder="Password" required>
      </div>
      <button type="submit" name="submit" class="btn btn-primary btn-block">Log in</button>
    </form>
  </div>
</template>

<script>
/*eslint-disable*/

import Flash from '@/components/Flash.vue';

export default {
  name: 'Login',
  components: {
    Flash
  },
  data() {
    return {
      error: '',
      message: '',
    };
  },
  methods: {
    LoginUser() {
      console.log('Login function runs');

      const loginForm = document.getElementById('loginForm');
      const formData = new FormData(loginForm);

      fetch('http://localhost:5000/api/login', {
        method: 'POST',
        body: formData,
        headers: {},
        // credentials: 'same-origin',
      })
        .then((response) => {
            return response.json();
        })
        .then((jsonResponse) => {
            this.message = jsonResponse.status.message;

            if (jsonResponse.status.userid){
              sessionStorage.setItem('usid', jsonResponse.status.userid);
              sessionStorage.setItem('crtid', jsonResponse.status.cartid);
              this.$router.push('/items');
              console.log(jsonResponse);
            } else {
                console.log(jsonResponse);
            }
            // this.$router.push('/users/' + jsonResponse.status.userid + '/cart');
        })
        .catch((error) => {
          console.log(error);
          this.error = error;
        });
    },
  },
};
/* eslint-enable */
</script>
<style>
.login-form {
  background: white;
}
div.login-form{
  height: 20%;
  width: 500px;
  margin: 200px auto;
  padding: 50px;
  border: 2px solid #009F6B;
  border-radius: 5px;
}

button{
  margin-top: 10px;
}
</style>
