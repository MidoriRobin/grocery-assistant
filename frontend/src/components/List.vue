<template>
  <div class="list-items-page">
    <h2>{{ listInfo.name }}</h2>
    <div class="cont">
      <table class="list">
        <thead>
          <tr>
            <th class="sticky">Product</th>
            <th class="sticky">Item Price</th>
          </tr>
        </thead>
        <tbody class="body-area">
          <tr v-for="listItem in list" :key="listItem.id">
            <td>
              <!-- <img src="../assets/None.jpg"/> -->
              <p>{{listItem.Item.item_name}}</p>
            </td>
            <td>${{listItem.Item.cost}}</td>
            <td>
              <button class="rem-bttn"
              @click="removeItem(listItem.item_id)">Remove from list</button>
              <button class="rem-bttn"
              @click="addToCart(listItem.item_id, listItem.qty)">add to cart</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="nav-area">
      <button @click="$router.push('/lists')">Back</button>
      <button
      @click="goToCart()">
      To Cart</button>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "Lists",
  data: () => ({
    list: [],
    listInfo: '',
    message: '',
    error: '',
  }),

  methods: {

    getList: function() {
      console.log("fetching list items");
      let usid = sessionStorage.getItem("usid");
      let resp = '';

      fetch('http://localhost:5000/api/users/' + usid + '/lists/' +
      this.$route.params.listid, {
          method: 'GET',
          headers: {},
      })
      .then(function (response) {
          resp = response.status;
          return response.json();
      })
      .then((jsonResponse) => {
          console.log(jsonResponse.status.message);
          this.message = jsonResponse.status.message;
          this.list = jsonResponse.status.items;
          this.listInfo = jsonResponse.status.list;

      })
      .catch(function (error) {
          console.log(error);
      });
    },

    addToCart: function(itemid,qty) {
        console.log("adding item to cart");
        let cart = sessionStorage.getItem('crtid');
        let resp = '';

        fetch('http://localhost:5000/api/items/' +
          itemid + '/' + qty + '/cart/' + cart, {
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

    removeItem: function(itemid) {
        console.log("Removing item from cart")
        let usid = sessionStorage.getItem('usid');
        let crtid = sessionStorage.getItem('crtid');
        let resp = '';

        console.log(itemid);
        fetch('http://localhost:5000/api/users/' + usid + '/cart/' + crtid + '/'+ itemid, {
            method: 'DELETE',
            headers: {},
        })
        .then(function (response) {
            resp = response.status;
            return response.json();
        })
        .then((jsonResponse) => {
            console.log(jsonResponse);

            if(resp === 201) {
              console.log("OK, deleted from cart");
              this.getItems();
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
  },
  created: function () {
    console.log("lists page");
    this.getList();
  }
};
/* eslint-enable */
</script>

<style>
div.list-items-page {
  display: grid;
  grid-template-rows: 20% 10% 60% 10%;
  border: 2px solid black;
  height: 1000px;
  width: 80%;
  margin: 0 auto;
}

div.cont {
  grid-row: 3 / 4;
  border: 1px solid #464654;
  max-height: inherit;
  overflow-y: scroll;
  width: 80%;
  margin: 0 auto;
}

table.list {
  border-collapse: collapse;
  border: solid 2px black;
  width: 100%;
  table-layout: fixed;

}

button.rem-bttn {
  border-radius: 5px;
  border: 1px solid #F35B6F;
  transition-duration: 0.4s;
  /* background-color: grey; */
}

button.rem-bttn:hover{
  background-color: #F35B6F;
  color: white
}

div.nav-area {
  grid-row: 4 / 5;
}

th,td {
  border: 1px solid black;
}

/* thead {
  height: 10%;
} */

thead {
  height: 10%;
  border-bottom: 2px solid black;
}

tbody {
  height: 90%;
}

tr {
  height: 50px;

}

tr:nth-child(even) {background-color: #46465446;}

.body-area {
  max-height: inherit;
  max-width: inherit;

}

.sticky {
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0
}

</style>
