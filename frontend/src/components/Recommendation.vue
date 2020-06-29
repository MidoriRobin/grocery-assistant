<template>
  <div class="recomm">
    <ul class="item-list" v-if="recomm">
      <li v-for="item in recomm" :key="item.id">
        <router-link :to="{ name: 'SingleItem', params: { itemid: item.item_id }}">
          <img @click="goToItem(item.item_id)" class="plpic" src="../assets/None.jpg" alt="">
        </router-link>
        <div>
          <h5>{{item.item_name}}</h5>
          <p>{{item.desc_item}}</p>
        </div>
      </li>
    </ul>
    <div v-else>
      <p>No recommendations as yet</p>
    </div>
  </div>
</template>
<!-- change to comply with your preferred JS standard -->
<script>
/* eslint-disable */
export default {
  name: "Recomm",
  data: () => ({
    recomm: [],
    message: '',
    error: ''
  }),

  methods: {
    getRecommendations: function() {
      console.log("fetching recommendations");
      let usid = sessionStorage.getItem("usid");
      let resp = ''

      fetch('http://localhost:5000/api/TryThese/' + usid,{
          method: 'GET',
          headers: {},
      })
      .then(function (response) {
          resp = response.status;
          return response.json();
      })
      .then((jsonResponse) => {
          console.log(jsonResponse.status.items);
          this.recomm = jsonResponse.status.items;
      })
      .catch(function (error) {
          console.log(error);
      });
    },

    goToItem: function(itemid) {
        console.log("Navigating to item page..");
        // let meid = sessionStorage.getItem('usid');
        // let usid = sessionStorage.getItem('usid');
        this.$router.push('/items/' + itemid);
    },
  },

  created: function () {
    console.log("reommendations page");
    this.getRecommendations();
  }
};
/* eslint-enable */
</script>

<style>

div.recomm {
  display: grid;
  grid-template-rows: 40% 60%;
  grid-row-gap: 20px;
  border: 2px solid black;
  /* height: 1000px; */
  width: 80%;
  margin: 50px auto;
}

ul.item-list {
  grid-row: 2 / 3;
  grid-column: 2 / 3;
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  grid-column-gap: 50px;
  grid-row-gap: 60px;
}

ul.item-list li{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-top-style: solid;
    border-top-color: blue;
    border-radius: 10px;
    box-shadow: 1px 3px 4px gray;
    height: 400px;
    width: 300px;
}

.item-list div{
  grid-column: 2;
  padding-top: 20px;
  padding-bottom: auto;
}

.item-list img.plpic{
  width: 200px;
  height: 180px;
}

.item-list button{
  grid-column: 3;
  margin-top: auto;
  margin-bottom: auto;
  height: 50px;
}

button{
  color: #011627;
  border-radius: 5px;
  border: 1px solid #FF3366;
  padding: 5px;
  padding-left: 10px;
  padding-right: 10px;
  transition-duration: 0.4s;
}

button:hover{
  background-color: #FF3366;
  color: #011627;
}

button.add,button.sub {
  height: 30px;
}
</style>
