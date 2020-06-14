 <!-- eslint-disable  -->
<template>
  <div>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  name: 'Test',
  data() {
    return {
      message: '',
    };
  },
  methods: {
    getMsg: function() {
      console.log("Test function runs")

      fetch('http://localhost:5000/api/ping', {
          method: 'GET',
      })
      .then(function (response){
          return response.json();
      })
      .then(function (jsonResponse) {
          console.log(jsonResponse);
      })
      .catch(function (error) {
          console.log(error);
      });
    }
  },
  created: function () {
    console.log("Entered the test page");
    this.getMsg();
  },
};
</script>
 <!-- eslint-enable  -->
