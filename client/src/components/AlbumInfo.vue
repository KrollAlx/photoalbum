<template>
  <v-card height="400" width="256">
    <v-navigation-drawer permanent absolute>
        <v-list-item>
            <v-list-item-content>
                <v-list-item-title>
                    Инфомация об альбоме
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>

        <v-list dense nav>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title>Владелец: {{album.owner}}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title>Название: {{album.title}}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title>Количество фото: {{album.photo_count}}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title>Лайки: {{album.likes}}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title>Комментариев: {{album.comments}}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
        
        <v-divider></v-divider>

        <v-list dense nav>
            <v-list-item>
                <v-list-item-icon>
                    <v-btn class="ml-0"
                        fab dark x-small color="green"
                        @click="showPhotoForm"
                    >
                        <v-icon dark>mdi-plus</v-icon>
                    </v-btn>                                  
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title>Добавить фото</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-icon>
                    <v-btn class="ml-0"
                        fab dark x-small color="red"     
                        @click="showDeleteAlbum"                   
                    >
                        <v-icon dark>mdi-delete</v-icon>
                    </v-btn>                                  
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title>Удалить альбом</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</v-card>
</template>

<script>
import { mapMutations, mapState } from 'vuex';

export default {
    computed: {
        ...mapState({
            album: state => state.photos.currentAlbum
        })
    },
    methods: {
        ...mapMutations("photos", ["showPhotoForm"]),
        showDeleteAlbum() {
            this.$emit("deleteAlbum");
        }
    }
}
</script>