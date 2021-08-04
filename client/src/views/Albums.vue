<template>
  <v-container>
      <v-row>
          <v-app-bar
            color="green"
            dark            
          >
            <albums-nav/>

            <v-spacer></v-spacer>

            <span class="mr-3">Найти альбом</span>               
            <v-text-field 
              prepend-inner-icon="mdi-magnify"
              solo clearable dense hide-details background-color="light-green"
              v-model="filter"
            ></v-text-field> 

            <v-spacer></v-spacer>  

            <user-profile/>
          </v-app-bar>
      </v-row>
      <v-row>
        <v-col cols="4"
          v-for="album in filteredAlbums"
          :key="album.id">
          <album-preview :album="album"/>
        </v-col>
        <v-col cols="4" v-if="$route.query.popular != 'true'">
          <v-btn class="mx-2"
            fab dark color="green"
            @click="showAlbumForm">
            <v-icon dark>mdi-plus</v-icon>
          </v-btn>  
          <span>Создать альбом</span>        
        </v-col>   
      </v-row>

      <create-album-form />
  </v-container>
</template>

<script>
import UserProfile from "../components/UserProfile.vue"
import AlbumsNav from "../components/AlbumsNav.vue"
import AlbumPreview from "../components/AlbumPreview.vue"
import CreateAlbumForm from "../components/CreateAlbumForm.vue"
import {mapState, mapMutations, mapActions} from 'vuex'

export default {
  data: () => ({
    filter: ""
  }),
  computed: {
    ...mapState({
      albums: state => state.albums.albums
    }),
    filteredAlbums() {
      return this.filter ? this.albums.filter(a => a.title.includes(this.filter)) : this.albums;
    }
  },
  mounted() {
    this.getAlbumsList(this.$route);
  },
  methods: {
    ...mapMutations('albums', ['showAlbumForm']),
    ...mapActions('albums', ['getAlbums', 'getPopularAlbums']),
    getAlbumsList(route) {
      if (route.query.popular != 'true') {
        this.getAlbums();
      }
      else {
        this.getPopularAlbums();
      }
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.getAlbumsList(to);
    next();
  },
  components: {
    UserProfile,
    AlbumsNav,
    AlbumPreview,
    CreateAlbumForm
  }
}
</script>