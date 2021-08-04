import {http} from './http'
import store from '../store';

export default {
    getPhotos(album_id, success) {
        http.get(album_id + "/photo", {
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
    createPhoto(album_id, photo, success) {
        http.post(album_id + "/photo", photo, {
            headers: {
                'Authorization': `Token ${store.getters['auth/getAuthToken']}`,
                'Content-Type': 'multipart/form-data'
            }
        })
        .then(res => {
            success(res);
        })
        .catch(e => {
            console.log(e);
        });
    },
    updatePhoto(album_id, photo_id, photo, success) {
        http.put(album_id + "/photo/" + photo_id, photo, {
            headers: {
                'Authorization': `Token ${store.getters['auth/getAuthToken']}`,
                'Content-Type': 'multipart/form-data'
            }
        })
        .then(res => {
            success(res);
        })
        .catch(e => {
            console.log(e);
        });
    },
    deletePhoto(album_id, photo_id, success) {
        http.delete(album_id + "/photo/" + photo_id, {
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
    likePhoto(photo_id, success) {
        http.post(photo_id + "/like", {}, {
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
    sendComment(photo_id, text, success) {
        http.post(photo_id + "/comments", { text }, {
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