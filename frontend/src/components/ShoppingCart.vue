<template>
  <div class="cart-page">
    <div class="blank-bar">
      <h1>Shopping Cart</h1>
      <div class="bar">

      </div>
    </div>
    <div class="status-bar"></div>
    <div class="cart-cont">
      <table class="cart">
        <thead>
          <tr>
            <th class="sticky">Qty</th>
            <th class="sticky">Product</th>
            <th class="sticky">Item Price</th>
            <th class="sticky">Total</th>
          </tr>
        </thead>
        <tbody class="body-area">
          <tr v-for="item in cart" :key="item.id">
            <td>{{item.quantity}}</td>
            <td>
              <!-- <img src="../assets/None.jpg"/> -->
              <p>{{item.Item.item_name}}</p>
            </td>
            <td>${{item.Item.cost}}</td>
            <td>
              <p>$150.00</p>
              <button class="rem-bttn" @click="removeItem(item.item_id)">Remove from cart</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="checkout-area">
      <button>Proceed to checkout</button>
    </div>
  </div>
</template>
<!-- change to comply with your preferred JS standard -->
<script>
/* eslint-disable */
// import Navigation from '@/components/Navigation.vue'

export default {
  name: 'ShoppingCart',
  data: () => ({
    message: '',
    error: '',
    cart: [],
  }),

  methods: {
    getItems: function() {
      console.log("Fetching items from cart")

      fetch('http://localhost:5000/api/users/' + this.$route.params.userid + '/cart', {
          method: 'GET',
          headers: {},
      })
      .then(function (response) {
          return response.json();
      })
      .then((jsonResponse) => {
          this.cart = jsonResponse.status.cart;
          console.log(jsonResponse);
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
    placeOrder: function() {
        console.log("Checking out cart..")

        fetch('')
    },

    calculateTtl: function(quant,price) {
      console.log("calculaating..")
    }
  },
  created: function () {
    console.log("Fetching items for the user's cart");
    this.getItems();
  }
};
/* eslint-enable */
</script>
<style>
div.cart-page {
  display: grid;
  grid-template-rows: 20% 10% 60% 10%;
  border: 2px solid black;
  height: 1000px;
  width: 80%;
  margin: 0 auto;
  background: white;
}

div.blank-bar {
  grid-row: 1 / 2;
}

div.status {
  grid-row: 2 / 3;
}

div.cart-cont {
  grid-row: 3 / 4;
  border: 1px solid #464654;
  max-height: inherit;
  overflow-y: scroll;
  width: 80%;
  margin: 0 auto;
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

div.checkout-area {
  grid-row: 4 / 5;
}

div.checkout-area > button {
    color: white;
    background-color: #32a852;
    border-radius: 5px;
    border-style: none;
    padding: 20px;
    margin: 20px;
}

table.cart {
  border-collapse: collapse;
  border: solid 2px black;
  width: 100%;
  table-layout: fixed;

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


img {
  width: 100px;
}
</style>
