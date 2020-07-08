<template>
  <div class="recomm">
    <div class="recomm-header">
      <h3>Recommendations</h3>
      <Flash :message="message"/>
      <div class="filtr">
        <select v-model="catgry">
          <option disabled value="">Diet Pref</option>
          <option value="0">Default Pref</option>
          <option value="1">Vegetarian</option>
          <option value="2">High Carb</option>
          <option value="3">Low Carb</option>
          <option value="4">High Protien</option>
          <option value="5">Meat Lover</option>
          <option value="6">Pescatarian</option>
        </select>
        <button @click="filterRecommendations">Filter by</button>
      </div>
    </div>
    <ul class="recom-list" v-if="recomm != []">
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
import Flash from '@/components/Flash.vue'

export default {
  name: "Recomm",
  components: {
    Flash
  },
  data: () => ({
    recomm: [],
    message: '',
    error: '',
    catgry: ''
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

    filterRecommendations: function() {
      console.log("filtering recommendations");
      let usid = sessionStorage.getItem("usid");
      let resp = '';

      if (this.catgry > 0) {

        fetch('http://localhost:5000/api/TryThese/' + usid +
        '/' + this.catgry,{
          method: 'GET',
          headers: {},
        })
        .then(function (response) {
          resp = response.status;
          return response.json();
        })
        .then((jsonResponse) => {
          console.log(jsonResponse.status.items);

          if (jsonResponse.status.items === []){
            this.message = jsonResponse.status.message;
          } else {
            this.recomm = jsonResponse.status.items;
          };
        })
        .catch(function (error) {
          console.log(error);
        });
      } else {
        this.getRecommendations();
      }
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
  grid-template-rows: 10% 40% 50%;
  grid-row-gap: 20px;
  border: 2px solid black;
  /* height: 1000px; */
  width: 80%;
  margin: 50px auto;
  background-color: white;
}

div.recomm-header {
  grid-row: 2 / 3;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-bottom: 2px solid black;
}

div.recomm-header > h3 {

}

ul.recom-list {
  grid-row: 3 / 4;
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  grid-column-gap: 50px;
  grid-row-gap: 60px;
  padding-top: 25px;
}

ul.recom-list li{
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

.recom-list div{
  grid-column: 2;
  padding-top: 20px;
  padding-bottom: auto;
}

.recom-list img.plpic{
  width: 200px;
  height: 180px;
}

.recom-list button{
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
