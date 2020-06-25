<template>
  <div class="signup-page">
    <h3> Sign-Up </h3>
    <form class="form-sign" @submit.prevent="SignupUser" id="signForm" method="post">
      <div>
        <label>First Name: </label>
        <input type="text" name="firstname">
      </div>
      <div>
        <label>Last Name: </label>
        <input type="text" name="lastname">
      </div>
      <div>
        <label>Gender: </label>
        <select name="gender">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>
      <div>
        <label>Email: </label>
        <input type="email" name="email" required>
      </div>
      <div>
        <label>Phone: </label>
        <input type="text" name="phone" required>
      </div>
      <div>
        <label>City: </label>
        <input type="text" name="city" required>
      </div>
      <div>
        <label>Street: </label>
        <input type="text" name="street" required>
      </div>
      <div>
        <label>House Hold Size: </label>
        <input type="number" name="hhsize" required>
      </div>
      <div>
        <label>Adults in House: </label>
        <input type="number" name="adlts" required>
      </div>
      <div>
        <label>Children in House: </label>
        <input type="number" name="kids" required>
      </div>
      <div>
        <label>Marital Status: </label>
        <select name="maritalstat">
          <option value="single">Single</option>
          <option value="married">Married</option>
        </select>
      </div>
      <div>
        <label>Diet Preference: </label>
        <input type="text" name="dietpref" required>
      </div>
      <div>
        <label>Password: </label>
        <input type="password" name="password" required>
      </div>
      <div class="submit-btn">
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
/*eslint-disable*/
export default {
  name: 'Signup',
  data() {
    return {
      error: '',
      message: '',
    };
  },
  methods: {
    SignupUser() {
      console.log('Signup function runs');

      const signupForm = document.getElementById('signForm');
      const formData = new FormData(signForm);

      fetch('http://localhost:5000/api/signup', {
        method: 'POST',
        body: formData,
        headers: {},
        // credentials: 'same-origin',
      })
        .then((response) => {
            return response.json();
        })
        .then((jsonResponse) => {
            console.log(jsonResponse);
            this.$router.push('/');
        })
        .catch((error) => {
          console.log(error);
          this.error = error;
        });
    },
  },
};
</script>

<style>

form > div {
  padding-top: 10px;

}

.signup-page {
  width: 50%;
  background-color: white;
  margin-left: auto;
  margin-right: auto;
  font-weight: bold;
  padding-left: 20px;
  padding-right: 20px;
  font-size: 110%;
  margin-bottom: 30px;
  margin-top: 60px;
  padding-bottom: 50px;
}

.signup-page h3{
  text-align: center;
}

div.submit-btn > button{
  background-color: #4CAF50;
  border: none;
  color: white;
  text-align: center;
  margin-top: 20px;
  height: 50px;
  width: 200px;
  border-radius: 8px;
}

div.submit-btn > button:hover{
  background-color: white;
  border: 3px solid #4CAF50;
  color: #4CAF50;
}
</style>
