<!-- displays all the items in an aisle -->
<template>
  <div class="items-page">
    <div class="status-area">
      <h3> Products </h3>
      <div class="recom-area">
        <p> To make this a special experience for you we've prepared some recommendations</p>
        <button @click="$router.push('/trythese')"> See Recommendations </button>
      </div>
    </div>
    <div class="menu">
      <h4> Menu </h4>
      <ul class="aisles">
        <li>
          <div>
            <h5>Aisle 1</h5>
            <p>
              Description
            </p>
          </div>
          <button>go to Aisle</button>
        </li>
        <li>
          <h5>Aisle 2</h5>
          <p>
            Description
          </p>
          <button>go to Aisle</button>
        </li>
        <li>
          <h5>Aisle 3</h5>
          <p>
            Description
          </p>
          <button>go to Aisle</button>
        </li>
      </ul>
    </div>
    <ul class="item-list">
      <li v-for="(item,index) in items" :key="item.id">
        <router-link :to="{ name: 'SingleItem', params: { itemid: item.item_id }}">
          <img @click="goToItem(item.item_id)" class="plpic" src="../assets/None.jpg" alt="">
        </router-link>
        <div>
          <h5>{{item.item_name}}</h5>
          <p>{{item.desc_item}}</p>
        </div>
        <div class="cart-area">
          <input type="number" id="qty" name="quantity" value="0"
          v-model="item_qty[index].value" readonly/>
          <button type="button" @click="incr(index)" class="add"> + </button>
          <button type="button" @click="decr(index)" class="sub"> - </button>
          <button type="button" @click="addToCart(item.item_id,index)"
          name="profile">Add to cart</button>
        </div>
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
      item_qty: [{value:1},{value:1},{value:1},{value:1},{value:1},{value:1},{value:1},{value:1},{value:1},{value:1}],
  }),

  methods: {
    getItems: function() {
      console.log("Viewing all items..");
      let resp = '';
      fetch('http://localhost:5000/api/products?=page2',{
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

    addToCart: function(itemid,index) {
        console.log("adding item to cart");
        let cart = sessionStorage.getItem('crtid');
        let resp = '';

        fetch('http://localhost:5000/api/items/' +
          itemid + '/' + this.item_qty[index].value + '/cart/' + cart, {
              method: 'POST',
              headers: {},
          })
          .then(function (response) {
              resp = response.status;
              return response.json();
          })
          .then((jsonResponse) => {
              console.log(jsonResponse);

              if(resp === 201) {
                console.log("OK, item added");
                this.item_qty[index].value = 0;
              } else {
                console.log("Not OK");
              }
          })
          .catch(function (error) {
              console.log(error);
          });
    },

    incr: function(index) {
        console.log("incrementing quantity");
        this.item_qty[index].value = this.item_qty[index].value + 1;
        console.log(this.item_qty[index].value);
        // return qty
    },

    decr: function(index) {
        console.log("decrementing quantity");
        if (this.item_qty[index].value < 1) {
          console.log("quantity less than 1!");
        } else {
          this.item_qty[index].value = this.item_qty[index].value - 1;
        }

        console.log(this.item_qty[index].value);
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
  grid-template-rows: 40% 60%;
  grid-template-columns:20% 80%;
  grid-row-gap: 20px;
  border: 2px solid black;
  /* height: 1000px; */
  width: 80%;
  margin: 50px auto;
}

div.status-area {
  grid-row: 1 / 2;
  grid-column: 1 / 3;
  height: inherit;
  width: inherit;
  margin: 0 auto;
}

div.recom-area {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

div.recom-area > p {
  margin-right: 10px;
}

div.menu {
  grid-row: 2 / 3;
  grid-column: 1 / 2;
  border: 2px solid black;

}

h4 {
  height: 30px;
  width: 70%;
  padding: 5px;
  border-bottom: 3px solid grey;
  margin: 10px auto;
}

div.menu > ul {
  padding: 0;
}

ul.aisles > li {
  width: 70%;
  margin: 10px auto;
  padding: 10px;
  border-bottom: 1px solid grey;
}

ul.item-list{
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
