import {http} from './http'

export default {
    signIn(username, password, success, error) {
        http.post("auth/login", { username, password })
            .then(res => {
                success(res);
            })
            .catch(e => {
                error(e);
            });
    },
    signUp(username, password, success, error) {
        http.post("auth/registration", { username, password })
            .then(res => {
                success(res);
            })
            .catch(e => {
                error(e);
            });
    }
}