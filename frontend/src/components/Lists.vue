<template>
  <div class="list-page">
    <h2>Shopping lists</h2>
    <div class="list-area">
      <ul class="lists">
        <li v-for="list in lists" :key="list.id">
          <div>
            <h3>{{ list.name }}</h3>
            <p>Made on: {{ list.date_created}}</p>
          </div>
          <button @click="goToList(list.list_id)"> View List </button>
        </li>
      </ul>
    </div>
    <form class="listform" @submit.prevent="makeList" id="listForm" method="post">
      <div class="form-group">
        <h4> Make a new list</h4>
        <label for="name" class="sr-only">List Name: </label>
        <input type="text" id="list-name" name="name" class="form-control"
        placeholder="Name of list" required>
        <button type="submit" > Make list </button>
      </div>
    </form>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "Lists",
  data: () => ({
    lists: [],
    message: '',
    error: ''
  }),

  methods: {

    getLists: function() {
      console.log("fetching recommendations");
      let usid = sessionStorage.getItem("usid");
      let resp = ''

      fetch('http://localhost:5000/api/users/' + usid + '/lists',{
          method: 'GET',
          headers: {},
      })
      .then(function (response) {
          resp = response.status;
          return response.json();
      })
      .then((jsonResponse) => {
          console.log(jsonResponse.status.lists);
          this.lists = jsonResponse.status.lists;
      })
      .catch(function (error) {
          console.log(error);
      });
    },

    makeList: function() {
      console.log("fetching recommendations");
      let listForm = document.getElementById('listForm');
      let formData = new FormData(listForm)
      let usid = sessionStorage.getItem("usid");
      let resp = ''

      fetch('http://localhost:5000/api/users/' + usid + '/lists',{
          method: 'POST',
          body: formData,
          headers: {},
      })
      .then(function (response) {
          resp = response.status;
          return response.json();
      })
      .then((jsonResponse) => {
          console.log(jsonResponse.status.message);
          this.message = jsonResponse.status.message;
          this.getLists();
      })
      .catch(function (error) {
          console.log(error);
      });
    },

    listToCart: function() {
      console.log("moving item to cart");
    },

    goToList: function(listid) {
        console.log("Navigating to item page..");
        this.$router.push('/lists/' + listid);
    },
  },

  created: function () {
    console.log("lists page");
    this.getLists();
  }
};
/* eslint-enable */
</script>

<style>

div.list-page {
  display: grid;
  grid-template-rows: 20% 80%;
  grid-template-columns: 80% 20%;
  border: 2px solid black;
  /* height: 1000px; */
  width: 80%;
  margin: 0 auto;
  margin-top: 50px;
  margin-bottom: 50px;
  background: white;
}

div.list-area {
  display: grid;
  grid-column: 1 / 2;
}

form#listForm {
  border-left: 2px solid black;
  border-radius: 10px;
}

ul.lists li{
  display: grid;
  grid-template-columns: 250px auto 200px;
  border-top-style: solid;
  border-top-color: blue;
  border-radius: 10px;
  box-shadow: 1px 3px 4px gray;
  padding: 10px;
  margin: 20px;
  height: 200px;
}

.lists button{
  grid-column: 3;
  margin-top: auto;
  margin-bottom: auto;
  height: 50px;
}
</style>
