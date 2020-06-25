<!-- displays all the items in an aisle -->
<template>
  <div class="items-page">
    <ul class="item-list">
      <li v-for="item in items" :key="item.id">
        <img class="plpic" src="../assets/None.jpg" alt="">
        <div>
          <h4>{{item.item_name}}</h4>
          <p>{{item.desc_item}}</p>
        </div>
        <button type="button" @click="goToItem(item.item_id)" name="profile">View Item</button>
      </li>
    </ul>
  </div>
</template>

<!-- change to comply with your preferred JS standard -->
<script>
/* eslint-disable */
export default {
  name: "Items",
  data: () => ({
      message: '',
      error: '',
      items: [],
      curr_page: '',
      prev_page: '',
      next_page: '',
  }),

  methods: {
    getItems: function() {
      console.log("Viewing all items..");
      let resp = '';
      fetch('http://localhost:5000/api/products',{
          method: 'GET',
          headers: {},
      })
      .then(function (response){
          resp = response.status;
          return response.json();
      })
      .then((jsonResponse) => {
          console.log(jsonResponse);
          this.items = jsonResponse.status.products;
          this.curr_page = jsonResponse.status.current_Page;
          this.prev_page = jsonResponse.status.prev_page;
          this.next_page = jsonResponse.status.next_page;
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
      console.log("entered the item page");
      this.getItems();
  }
};

/* eslint-enable */
</script>
<style>
div.items-page {
  display: grid;
  grid-template-rows: 50% 50%;
  border: 2px solid black;
  height: 1000px;
  width: 80%;
  margin: 0 auto;
}

ul.item-list{
  margin-top: 50px;
  list-style: none;
}

ul.item-list li{
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

.item-list div{
  grid-column: 2;
  padding-top: 20px;
  padding-bottom: auto;
}

.item-list img.plpic{
  grid-column: 1;
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

</style>
