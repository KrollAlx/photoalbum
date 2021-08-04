<template>
    <v-row>
        <v-col cols="auto">
            <v-dialog
                v-model="formActive"
                transition="dialog-bottom-transition"
                max-width="600"
                persistent
            >
                <v-form @submit.prevent="onCreate">
                    <v-card>
                        <v-card-title>
                            <span class="text-h5">Добавление фото</span>
                            <v-spacer></v-spacer>
                            <span>
                                <v-btn icon
                                    @click="hidePhotoForm">
                                    <v-icon dark color="black">mdi-close</v-icon>
                                </v-btn> 
                            </span>
                        </v-card-title>
                        <v-card-text>
                            <v-container>
                                <v-row>
                                    <v-col cols="12">
                                        <v-text-field
                                            v-model="title"
                                            label="Название"
                                            required
                                        ></v-text-field>
                                    </v-col>
                                    <v-col cols="12">
                                        <v-file-input
                                            v-model="img"
                                            label="Фото"
                                            prepend-icon="mdi-camera"
                                        ></v-file-input>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="success" type="submit">
                                Добавить
                            </v-btn>
                            <v-btn 
                                color="primary"
                                @click="hidePhotoForm"
                            >
                                Отмена
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-form>                
            </v-dialog>
        </v-col>
    </v-row>
</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex'

export default {
    data: () => ({
        title: "",
        img: null
    }),
    computed: {
        ...mapState({
            formActive: state => state.photos.photoFormActive
        })
    },
    methods: {
        ...mapMutations("photos", ["hidePhotoForm"]),
        ...mapActions("photos", ["createPhoto"]),
        onCreate() {            
            let formData = new FormData();
            formData.append("title", this.title);
            formData.append("image", this.img);
            
            this.createPhoto(formData);
            this.hidePhotoForm();
        }
    },
}
</script>