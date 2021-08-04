<template>
	<v-container style="height: 100%" class="justify-center pt-16">
		<v-row class="justify-center align-center">
			<v-col cols="4" align-self="center">
				<h2 class="text-center">Регистрация</h2>
				<v-form @submit.prevent="onSignUp">
					<v-text-field
							v-model="$v.username.$model"
							label="Логин"
					></v-text-field>
					<div class="error" v-if="$v.username.$dirty && !$v.username.required">Заполните поле "Логин"</div>
					<v-text-field
							v-model="$v.password1.$model"
							label="Пароль"
							type="password"
					></v-text-field>
					<div class="error" v-if="$v.password1.$dirty && !$v.password1.required">Заполните поле "Пароль"</div>
					<div class="error" v-if="$v.password1.$dirty && !$v.password1.minLength">
							Пароль должен быть длинной не менее {{ $v.password1.$params.minLength.min }} символов
					</div>
					<v-text-field
							v-model="$v.password2.$model"
							label="Повторите пароль"
							type="password"
					></v-text-field>
					<div class="error" v-if="$v.password2.$dirty && !$v.password2.required">
							Повторите пароль
					</div>
					<div class="error" v-if="$v.password2.$dirty && $v.password1.$model != $v.password2.$model">
							Пароли должны совпадать
					</div>
					<v-btn type="submit" color="success" dark block>Зарегистрироваться</v-btn>
					<div class="error" v-if="$store.getters['auth/getSignUpErrorMessage']">
                        {{ $store.getters['auth/getSignUpErrorMessage'] }}						
                    </div>
					<v-btn color="primary" dark block class="mt-4"
							@click="$router.push('/')">
							Войти                        
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
		password1: '',
		password2: ''
	}),
	validations: {
		username: {
			required
		},
		password1: {
			required,
			minLength: minLength(4)
		},
		password2: {
			required         
		}
	},
	methods: {
		onSignUp() {
			if (!this.$v.$invalid) {
				this.$store.dispatch("auth/signUp", {
                    username: this.username, 
                    password: this.password1
                });    
			}
		}
	}
}
</script>
