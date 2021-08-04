import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import albums from './modules/albums'
import photos from './modules/photos'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    albums,
    photos
  }
})
