<template>
  <div class="signup-page">
    <Flash :message="message"/>
    <Flash :error="error"/>
    <h3> Sign-Up </h3>
    <hr>
    <form class="form-sign" @submit.prevent="SignupUser" id="signForm" method="post">
      <div>
        <label for="firstname">First Name</label>
        <input type="text" name="firstname">
      </div>
      <div>
        <label for="lastname">Last Name </label>
        <input type="text" name="lastname">
      </div>
      <div>
        <label for="gender">Gender </label>
        <select name="gender">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>
      <div>
        <label for="email">Email</label>
        <input type="email" name="email" required>
      </div>
      <div>
        <label for="phone">Phone </label>
        <input type="text" name="phone" required>
      </div>
      <div>
        <label for="city">City </label>
        <input type="text" name="city" required>
      </div>
      <div>
        <label for="street">Street </label>
        <input type="text" name="street" required>
      </div>
      <div>
        <label for="hhsize">House Hold Size </label>
        <input type="number" name="hhsize" required>
      </div>
      <div>
        <label for="adlts">Adults in House</label>
        <input type="number" name="adlts" required>
      </div>
      <div>
        <label for="kids">Children in House </label>
        <input type="number" name="kids" required>
      </div>
      <div>
        <label for="maritalstat">Marital Status </label>
        <select name="maritalstat">
          <option value="single">Single</option>
          <option value="married">Married</option>
        </select>
      </div>
      <div>
        <label for="dietpref">Diet Preference: </label>
        <select name="dietpref">
          <option value="Vegetarian">Vegetarian</option>
          <option value="High Carb">High Carb</option>
          <option value="Low Carb">Low Carb</option>
          <option value="High Protien">High Protien</option>
          <option value="Meat Lover">Meat Lover</option>
          <option value="Pescatarian">Pescatarian</option>
        </select>
      </div>
      <div>
        <label for="password">Password</label>
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

import Flash from '@/components/Flash.vue';
export default {
  name: 'Signup',
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
            this.message = jsonResponse.status.message
            this.$router.push('/login');
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
input, select{
  display: inline-block;
  background-color: white;
  width: 60%;
  border:none;
  background-color: #D3D3D3;
  height: 30px;
  radius: 5px;
  align-self: center;

}

div > label, div >input{
  margin-bottom: 10px;
}

div > label{
  display: inline-block;
  width: 20%;
  text-align: left;
}
.signup-page {
  /* background-image: url("background2.jpg"); */
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
  box-shadow: 5px 6px #90ee90;
  border:none;
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
