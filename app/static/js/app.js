/* Add your Application JavaScript */
// console.log('this is some JavaScript code');
//
// function notify() {
//   alert('in here I will do something');
// }

// notify();
const Landing = Vue.component('landing-page',{
  template:`
  `,
  data: function (){
    return { }
  }
})


const router = new VueRouter({
  mode:'history',
  routes: [
    {path:'/', componenet: Home},
    {path:'/landing', component:Landing}
  ]
})

let app = new Vue({
    el: '#app',
    router
});
