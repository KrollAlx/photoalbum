import auth_service from "../../api/auth_service";
import router from "../../router";

export default {
    namespaced: true,
    state: {
        username: "",
        authToken: "",
        signInError: "",
        signUpError: ""
    },
    mutations: {
        setUsername(state, username) {
            state.username = username;
        },
        setAuthToken(state, token) {
            state.authToken = token;
        },
        setSignInErrorMessage(state, message) {
            state.signInError = message;
        },
        setSignUpErrorMessage(state, message) {
            state.signUpError = message;
        }
    },
    actions: {
        signIn(context, {username, password}) {
            auth_service.signIn(username, password, res => {
                console.log(res);
                context.commit("setUsername", username);
                context.commit("setAuthToken", res.data.token);
                context.commit("setSignInErrorMessage", "");
                router.push({path: "albums", query: {popular: false}});
            }, e => {
                context.commit("setSignInErrorMessage", "Указан неверный логин или пароль");
            });
        },
        signUp(context, {username, password}) {
            auth_service.signUp(username, password, res => {
                console.log(res);
                context.commit("setSignUpErrorMessage", "");
                context.dispatch("signIn", {username, password});
            }, e => {
                context.commit("setSignUpErrorMessage", "Ошибка регистрации");
            });
        }
    },
    getters: {
        getSignInErrorMessage(state) {
            return state.signInError;
        },
        getSignUpErrorMessage(state) {
            return state.signUpError;
        },
        getUsername(state) {
            return state.username;
        },
        getAuthToken(state) {
            return state.authToken;
        }
    }
}