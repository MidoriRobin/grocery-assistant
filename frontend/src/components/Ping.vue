<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      fetch('http://localhost:5000/api/ping', {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((jsonResponse) => console.log(jsonResponse))
        .catch((error) => console.log(error));
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
