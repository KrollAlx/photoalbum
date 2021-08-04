<template>
    <v-row>
        <v-col cols="auto">
            <v-dialog
                v-model="formActive"
                transition="dialog-bottom-transition"
                max-width="300"
                persistent
            >
                <v-card>
                    <v-card-title>
                        Создание альбома
                    </v-card-title>
                    <v-card-text>
                        <v-form @submit.prevent="onCreate">
                            <v-text-field
                                label="Название альбома"
                                v-model="albumTitle"
                            ></v-text-field>
                            <v-row justify="space-around">
                                <v-btn
                                    type="submit"
                                    color="success"
                                >Создать</v-btn>
                                <v-btn 
                                    @click="hideDialog"
                                    color="primary"
                                >Отмена</v-btn>
                            </v-row>
                        </v-form>
                    </v-card-text>
                </v-card>                
            </v-dialog>
        </v-col>
    </v-row>
</template>

<script>
import { mapMutations, mapState, mapActions } from 'vuex';

export default {
    data: () => ({    
        albumTitle: ""
    }),
    computed: {
        ...mapState({
            formActive: state => state.albums.albumFormActive
        })
    },
    methods: {
        ...mapMutations('albums', ['hideAlbumForm']),
        ...mapActions('albums', ['createAlbum']),
        hideDialog() {
            this.albumTitle = "";
            this.hideAlbumForm();
        },
        onCreate() {                        
            this.createAlbum(this.albumTitle);
            this.albumTitle = "";
        }
    }
}
</script>
