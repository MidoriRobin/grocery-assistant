<template>
  <div class="login-form text-center">
    <h2>Please Log in</h2>
    <h4 v-if="error"> Error: {{ error }} </h4>
    <h5 v-if="message"> Message: {{ message }} </h5>
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
export default {
  name: 'Login',
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
            sessionStorage.setItem('usid', jsonResponse.status.userid);
            sessionStorage.setItem('crtid', jsonResponse.status.cartid);
            console.log(jsonResponse);
            this.$router.push('/users/' + jsonResponse.status.userid + '/cart');
        })
        .catch((error) => {
          console.log(error);
          this.error = error;
        });
    },
  },
};
</script>
