import {http} from './http'
import store from '../store';

export default {
    getAblums(success) {
        http.get("album", {
            headers: {
                'Authorization': `Token ${store.getters['auth/getAuthToken']}`
            }
        })
        .then(res => {
            success(res);
        })
        .catch(e => {
            console.log(e);
        });
    },
    getPopularAlbums(success) {
        http.get("popular-albums", {
            headers: {
                'Authorization': `Token ${store.getters['auth/getAuthToken']}`
            }
        })
        .then(res => {
            success(res);
        })
        .catch(e => {
            console.log(e);
        });
    },
    getAlbum(id, success) {
        http.get("album/" + id, {
            headers: {
                'Authorization': `Token ${store.getters['auth/getAuthToken']}`
            }
        })
        .then(res => {
            success(res);
        })
        .catch(e => {
            console.log(e);
        });
    },
    createAlbum(title, success){
        http.post("album", { title }, {
            headers: {
                'Authorization': `Token ${store.getters['auth/getAuthToken']}`
            }
        })
        .then(res => {
            success(res);
        })
        .catch(e => {
            console.log(e);
        });
    },
    deleteAlbum(album_id, success) {
        http.delete("album/" + album_id, {
            headers: {
                'Authorization': `Token ${store.getters['auth/getAuthToken']}`
            }
        })
        .then(res => {
            success(res);
        })
        .catch(e => {
            console.log(e);
        });
    }
}