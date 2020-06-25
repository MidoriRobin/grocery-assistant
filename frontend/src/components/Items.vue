<!-- displays all the items in an aisle -->
<template>
  <div class="display-items" >
    <div class="slide-selector"></div>
      <div v-for:"item in items" class="">
        <div class="display-img">

        </div>
        <div class="item-desc">

        </div>
        <button type="button" name="button"></button>
        <input type="text" name="item-quantity" value="">

      </div>

  </div>
</template>

<!-- change to comply with your preferred JS standard -->
<script>
/* eslint-disable*/
export default {
  name: '',
  data() {
    return {
      name: 'Giselle',
    };
  },
};
/* eslint-enable */
</script>

<style>
</style>
