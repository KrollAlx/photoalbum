import album_service from "../../api/album_service"
import photo_service from "../../api/photo_service"

export default {
    namespaced: true,
    state: {
        currentAlbum: {},
        photos: [],
        currentPhoto: {},
        photoFormActive: false,
        updateForm: false,
    },
    mutations: {
        setCurrentAlbum(state, album) {
            state.currentAlbum = album;
        },
        setCurrentPhoto(state, photoId) {
            state.currentPhoto = state.photos.find(p => p.id == photoId);
        },
        setPhotos(state, photos) {
            state.photos = photos;
        },
        showPhotoForm(state) {
            state.photoFormActive = true;
        },
        hidePhotoForm(state) {
            state.photoFormActive = false;
        },
        showUpdateForm(state) {
            state.updateForm = true;
        },
        hideUpdateForm(state) {
            state.updateForm = false;
        },
        addPhoto(state, photo) {
            state.photos.push(photo);
            state.currentAlbum.photo_count++;
        },
        updatePhoto(state, photo) {
            let targetPhoto = state.photos.find(p => p.id == photo.id);
            targetPhoto = photo;            
        },
        deletePhoto(state, photoId) {
            state.photos = state.photos.filter(p => p.id != photoId);
            state.currentAlbum.photo_count--;
        },
        likePhoto(state, like) {
            let targetPhoto = state.photos.find(p => p.id == like.photo);
            if (like.id) {
                targetPhoto.likes++;    
                state.currentAlbum.likes++;
            }
            else {
                targetPhoto.likes--;  
                state.currentAlbum.likes--;
            }
        },
        addComment(state, comment) {
            let targetPhoto = state.photos.find(p => p.id == comment.photo);
            targetPhoto.comments.push({
                author: comment.author,
                text: comment.text
            });
            targetPhoto.comments_count++;
            state.currentAlbum.comments++;
        }
    },
    actions: {
        getAlbum({ commit }, album_id) {
            album_service.getAlbum(album_id, res => {
                commit("setCurrentAlbum", res.data);
            });
        },
        getPhotos({ commit }, album_id) {
            photo_service.getPhotos(album_id, res => {
                commit("setPhotos", res.data);
            });
        },
        createPhoto({ commit, state }, photo) {
            photo_service.createPhoto(state.currentAlbum.id, photo, res => {
                console.log(res.data);
                commit("addPhoto", res.data);
            });
        },
        updatePhoto({ commit }, {albumId, photoId, photo}) {            
            photo_service.updatePhoto(albumId, photoId, photo, res => {
                commit("updatePhoto", res.data);
            });
        },
        deletePhoto({ commit }, {albumId, photoId}) {
            photo_service.deletePhoto(albumId, photoId, res => {
                commit("deletePhoto", photoId);
            });
        },
        likePhoto({ commit }, photoId) {
            photo_service.likePhoto(photoId, res => {
                console.log(res);
                commit("likePhoto", res.data);
            });
        },
        sendComment({ commit }, { photoId, commentText }) {
            photo_service.sendComment(photoId, commentText, res => {
                commit("addComment", res.data);
            });
        }
    }
}