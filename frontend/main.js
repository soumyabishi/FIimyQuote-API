import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import VueLocalStorage from 'vue-localstorage'

Vue.use(VueResource);
Vue.use(VueLocalStorage);

import'./assets/js/semantic.min.js'


import VueProgressiveImage from 'vue-progressive-image'

Vue.use(VueProgressiveImage, {
    placeholder: 'https://unsplash.it/1920/1080?image=20'
});

Vue.use(require('vue-shortkey'));
Vue.use(require('vue-cookies'));

// eslint-disable-next-line no-new
new Vue({
    el: '#app',
    render: h => h(App),
    localStorage: {
        filmy_quotes_user_added_dialogues: {
            type: Object,
            default: []
        },
    }
});
