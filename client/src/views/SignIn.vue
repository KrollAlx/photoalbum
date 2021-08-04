<template>
    <v-container style="height: 100%" class="justify-center pt-16">
        <v-row class="justify-center align-center">
            <v-col cols="4" align-self="center">
                <h2 class="text-center">Авторизация</h2>
                <v-form @submit.prevent="onSignIn">
                    <v-text-field
                        v-model="$v.username.$model"
                        label="Логин"
                    ></v-text-field>
                    <div class="error" v-if="$v.username.$dirty && !$v.username.required">Заполните поле "Логин"</div>
                    <v-text-field
                        v-model="$v.password.$model"
                        label="Пароль"
                        type="password"
                    ></v-text-field>
                    <div class="error" v-if="$v.password.$dirty && !$v.password.required">Заполните поле "Пароль"</div>
                    <div class="error" v-if="$v.password.$dirty && !$v.password.minLength">
                        Пароль должен быть длинной не менее {{ $v.password.$params.minLength.min }} символов
                    </div>
                    <v-btn type="submit" color="success" dark block>Войти</v-btn>
                    <div class="error" v-if="$store.getters['auth/getSignInErrorMessage']">
                        {{ $store.getters["auth/getSignInErrorMessage"] }}
                    </div>
                    <v-btn color="primary" dark block class="mt-4"
                        @click="$router.push('/sign-up')">
                        Регистрация                        
                    </v-btn>
                </v-form>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import {required, minLength} from 'vuelidate/lib/validators'

export default {
    data: () => ({
        username: '',
        password: ''
    }),
    validations: {
        username: {
            required
        },
        password: {
            required,
            minLength: minLength(4)
        }
    },
    methods: {
        onSignIn() {            
            if (!this.$v.$invalid) {
                this.$store.dispatch("auth/signIn", {
                    username: this.username, 
                    password: this.password
                });              
            }
        }
    }
}
</script>

<style>

.error {
    margin-top: 10px;
    margin-bottom: 10px;
    text-align: center;
    border-radius: 4px;
}

</style>