<!-- this page displays the details of an items, is a result of clicking 'Click for more!'  -->
<template>
  <div class="item-page">
    <Flash :message="message"/>
    <!-- <h1>This is the Single Item Page</h1> -->
    <div class="about-item">
      <div class="item-img">
        <img src="../assets/None.jpg"/>
      </div>
      <div class="about">
        <div class="item-info">
          <ul>
            <li><h4>{{item.item_name}}</h4></li>
            <li><p> Brand: {{ item.brand }} </p></li>
            <li><p> Price: ${{ item.cost }} </p></li>
            <li>
              <form class="form-review" @submit.prevent="reviewItem" id="reviewForm" method="post">
                <label for="rating">Rate: </label>
                <select name="rating">
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="4">4</option>
                  <option value="5">5</option>
                </select>
              </form>
            </li>
          </ul>
        </div>
        <button @click="scrllToReview">Leave a Review</button>
        <div class="item-desc">
          <h5>Description</h5>
          <p>
            {{ item.desc_item }}
          </p>
        </div>
        <div class="cart-ctrl">
            <input type="number" id="qty" name="quantity" value="0" v-model="qty" readonly/>
            <button type="button" @click="incr"> + </button>
            <button type="button" @click="decr"> - </button> <br>
            <button type="button" @click="addToCart">Add to cart</button>
        </div>
      </div>
    </div>
    <div class="nav-area">
      <div class="nav-buttons">
        <button @click="returnToItems">Back</button>
        <button @click="goToCart">To Cart</button>
      </div>
      <form class="form-review" @submit.prevent="reviewItem" id="reviewForm" method="post">
        <ul>
          <li>
            <textarea name="review" rows="10" cols="50" placeholder="Leave a review"></textarea>
          </li>
          <li>
            <label for="rating">Rating: </label>
            <select name="rating">
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
            </select>
          </li>
        </ul>
        <button type="submit"> Submit </button>
      </form>
    </div>
  </div>
</template>

<!-- change to comply with your preferred JS standard -->
<script>
/* eslint-disable */

import Flash from '@/components/Flash.vue'

export default {
  name: "SingleItem",
  components: {
    Flash
  },
  data: () => ({
    message: '',
    error: '',
    item: '',
    lists: '',
    qty: 1,
  }),

  methods: {
    getItem: function() {
      console.log("Viewing a single item..")
      let resp = ''
      fetch('http://localhost:5000/api/products/' + this.$route.params.itemid,{
          method: 'GET',
          headers: {}
      })
      .then(function (response){
          resp = response.status;
          return response.json();
      })
      .then((jsonResponse) => {
          console.log(jsonResponse.status.item);
          this.item = jsonResponse.status.item;
      })
      .catch(function (error) {
          console.log(error);
      });
    },

    reviewItem: function() {
        console.log("Reviewing item");

        let reviewForm = document.getElementById('reviewForm');
        let formData = new FormData(reviewForm);

        fetch('http://localhost:5000/api/items/' + this.$route.params.itemid + '/review/', {
            method: 'POST',
            body: formData,
            headers: {},
        })
        .then(function (response){
            return response.json();
        })
        .then((jsonResponse) => {
            this.message = jsonResponse.status.message;
            console.log(jsonResponse);
        })
        .catch(function (error) {
            console.log(error);
        });
    },

    scrllToReview: function() {
      let elmnt = document.getElementById('reviewForm');

      elmnt.scrollIntoView(true);
    },

    addToCart: function() {
        console.log("adding item to cart");
        let cart = sessionStorage.getItem('crtid');
        let resp = '';

        fetch('http://localhost:5000/api/items/' +
          this.item.item_id + '/' + this.qty + '/cart/' + cart, {
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
                this.message = jsonResponse.status.message;
                console.log("OK, item added");
                this.qty = 0;
              } else {
                console.log("Not OK");
              }
          })
          .catch(function (error) {
              console.log(error);
          });
    },

    goToCart: function() {
        console.log("Navigating to cart..");
        // let meid = sessionStorage.getItem('usid');
        let usid = sessionStorage.getItem('usid');
        this.$router.push('/users/' + usid + '/cart');
    },

    returnToItems: function() {
        console.log("returning to items..");
        this.$router.push('/items');
    },

    getLists: function() {
        console.log("Getting users lists");
        let usr = sessionStorage.getItem('usid');
        console.log(usr)
        fetch('http://localhost:5000/api/users/' + usr + '/lists',{
          method: 'GET',
          headers: {},
        })
        .then(function (response){
          return response.json();
        })
        .then((jsonResponse) => {
          console.log(jsonResponse)
          this.lists = jsonResponse.status.lists;
        })
        .catch(function (error) {
            console.log(error)
        });
    },

    incr: function() {
        console.log("incrementing quantity");
        this.qty = this.qty + 1;
        console.log(this.qty);

    },

    decr: function() {
        console.log("decrementing quantity");
        if (this.qty < 1) {
          console.log("quantity less than 1!");
        } else {
          this.qty = this.qty - 1;
        }

        console.log(this.qty);
    }
  },
  created: function () {
      console.log("Entered the item page");
      this.getItem();
      this.getLists();
  }
};

/* eslint-enable */
</script>
<style>
li {
  list-style-type: none;
}
div.item-page {
  display: grid;
  grid-template-rows: 50% 50%;
  border: 2px solid black;
  height: 1000px;
  width: 80%;
  margin: 0 auto;
  margin-top: 50px;
}

div.about-item {
  grid-row: 1 / 2;
  display: grid;
  grid-template-columns: 50% 50%;
}

div.item-img {
  border: 2px solid black;
}

div.item-img > img {
  height: 350px;
  width: 350px;
  margin: 50px auto;
}

div.about {
  display: grid;
  grid-template-rows: auto auto auto;
  grid-template-columns: 50% 50%;

}

div.item-info {
  grid-row: 1 / 2;
  grid-column: 1 / 2;
}

div.item-info > ul {
  list-style: None;
}

div.about > button {
  padding: 0;
  border-radius: 5px;
  border: 1px solid grey;
  height: 20%;
  width: 50%;
  margin: auto;
}

div.item-desc {
  grid-row: 2 / 3;
  grid-column: 1 / 3;

}

div.cart-ctrl {
  grid-row: 3 / 4;
  grid-column: 1 / 3;

}

div.nav-area {
  grid-row: 2 / 3;
  display: grid;
  grid-template-rows: 30% 70%;
}

div.nav-buttons {
  grid-row: 1 / 2;
  margin: 50px auto;
}

.cart-ctrl > button {
  border-radius: 5px;
  border: 1px solid grey;
}

</style>
