<template>
  <v-container>
      <v-row>
          <v-app-bar
            color="green"
            dark            
          >
            <albums-nav/>

            <v-spacer></v-spacer>  

            <user-profile/>
          </v-app-bar>
      </v-row>
      <v-row>        
        <v-col cols="3">
            <album-info
                @deleteAlbum="deleteAlbumDialog = true"
            />
        </v-col>
        <v-col cols="9">
            <v-list dense>
                <v-list-item 
                    v-for="photo in photos"
                    :key="photo.id"
                >
                    <v-list-item-content>                        
                        <v-card>
                            <v-list-item-title class="text-center mb-3 mt-3">{{photo.title}}</v-list-item-title>

                            <v-img height="425" :src="photo.image"/>

                            <v-divider></v-divider>

                            <v-row justify="space-around" class="mt-5 mb-5">
                                <v-btn icon dark large color="red"
                                    @click="like(photo.id)"
                                >
                                    <v-icon dark>mdi-heart</v-icon>
                                    <span>{{photo.likes}}</span>
                                </v-btn>

                                <v-btn icon dark large color="blue">
                                    <v-icon dark>mdi-comment</v-icon>
                                    <span>{{photo.comments_count}}</span>
                                </v-btn>                            

                                <v-menu                                    
                                    close-on-content-click
                                    top
                                    transition="scale-transition">
                                    <template v-slot:activator="{on, attrs}">
                                        <v-btn icon dark large color="black"
                                            v-bind="attrs"
                                            v-on="on">
                                            <v-icon dark>mdi-dots-horizontal</v-icon>
                                        </v-btn>
                                    </template>

                                    <v-list>
                                        <v-list-item>
                                            <v-btn 
                                                color="primary"
                                                @click="onEditPhoto(photo.id)"
                                            >Редактировать</v-btn>
                                        </v-list-item>
                                        <v-list-item>
                                            <v-btn color="error"
                                                @click="onDeletePhoto(photo.id)"
                                            >Удалить</v-btn>
                                        </v-list-item>
                                    </v-list>
                                </v-menu>                                
                            </v-row>

                            <v-divider></v-divider>

                            <v-list>
                                <v-list-item 
                                    v-for="comment in photo.comments"
                                    :key="comment.id"
                                >
                                    <v-list-item-content>
                                        <v-list-item-title>{{comment.author}}: {{comment.text}}</v-list-item-title>
                                    </v-list-item-content>
                                </v-list-item>
                            </v-list>
                            
                            <v-form class="ml-3 pr-5" @submit.prevent="leaveComment(photo.id)">
                                <v-row>
                                    <v-col cols="11">
                                        <v-text-field required
                                            v-model="commentText"
                                            label="Напишите комментарий"></v-text-field>
                                    </v-col>
                                    <v-col cols="1">
                                        <v-btn icon dark x-large type="submit"
                                            color="blue">
                                            <v-icon dark>mdi-arrow-right-drop-circle</v-icon>
                                        </v-btn>
                                    </v-col>
                                </v-row>                            
                            </v-form>
                        </v-card>
                    </v-list-item-content>
                </v-list-item>                
            </v-list>
        </v-col>
    </v-row>

    <add-photo-form />

    <delete-dialog
        :text="deleteAlbumText"
        v-model="deleteAlbumDialog"
        @confrim="onDeleteAlbum"
        @cancel="deleteAlbumDialog = false"
    />  

    <delete-dialog
        :text="deletePhotoText"
        v-model="deletePhotoDialog"
        @confrim="confirmDeletePhoto"
        @cancel="deletePhotoDialog = false"
    />  

    <update-photo-form />
  </v-container>
</template>

<script>
import UserProfile from "../components/UserProfile.vue"
import AlbumsNav from "../components/AlbumsNav.vue"
import AlbumInfo from "../components/AlbumInfo.vue"
import AddPhotoForm from "../components/AddPhotoForm.vue"
import UpdatePhotoForm from "../components/UpdatePhotoForm.vue"
import DeleteDialog from "../components/DeleteDialog.vue"
import { mapActions, mapMutations, mapState } from 'vuex'

export default {
    data: () => ({
        deleteAlbumText: "Удалить альбом?",
        deleteAlbumDialog: false,
        deletePhotoText: "Удалить фотографию?",
        deletePhotoDialog: false,
        commentText: ""
    }),
    computed : {
        ...mapState({           
            photos: state => state.photos.photos,
            currentPhoto: state => state.photos.currentPhoto         
        })
    },
    mounted() {
        this.getAlbum(this.$route.params.id);
        this.getPhotos(this.$route.params.id);
    },
    methods: {
        ...mapMutations("photos", ["showUpdateForm", "setCurrentPhoto"]),
        ...mapActions("photos", ["getAlbum", "getPhotos", "deletePhoto", "likePhoto", "sendComment"]), 
        ...mapActions("albums", ["deleteAlbum"]),       
        onDeleteAlbum() {
            this.deleteAlbum(this.$route.params.id);
            this.deleteAlbumDialog = false;
            this.$router.push('/albums?popular=false');
        },
        onEditPhoto(photoId) {
            this.setCurrentPhoto(photoId);
            this.showUpdateForm();
        },
        onDeletePhoto(photoId) {
            this.setCurrentPhoto(photoId);
            this.deletePhotoDialog = true;
        },
        confirmDeletePhoto() {
            this.deletePhoto({
                albumId: this.$route.params.id,
                photoId: this.currentPhoto.id
            });
            this.deletePhotoDialog = false;
        },
        like(photoId) {
            this.likePhoto(photoId);
        },
        leaveComment(photoId) {
            this.sendComment({ 
                photoId: photoId,
                commentText: this.commentText
            });
            this.commentText = "";
        }
    },
    components: {
        UserProfile,
        AlbumsNav,
        AlbumInfo,
        AddPhotoForm,
        DeleteDialog,
        UpdatePhotoForm
    }
}
</script>