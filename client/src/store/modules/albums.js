import album_service from "../../api/album_service"

export default {
    namespaced: true,
    state: {        
        albumFormActive: false,        
        albums: []
    },
    mutations: {
        setAlbums(state, albums) {
            state.albums = albums;
        },
        addAlbum(state, album) {
            state.albums.push(album);
        },
        showAlbumForm(state) {
            state.albumFormActive = true;
        },
        hideAlbumForm(state) {
            state.albumFormActive = false;
        }
    },
    actions: {
        getAlbums({ commit }) {
            album_service.getAblums((res) => {
                commit("setAlbums", res.data);
            });
        },
        getPopularAlbums({ commit }) {
            album_service.getPopularAlbums(res => {
                commit("setAlbums", res.data);
            });
        },
        createAlbum({ commit }, albumTitle) {
            commit("hideAlbumForm");
      
            album_service.createAlbum(albumTitle, (res) => {
                commit("addAlbum", res.data);
            });
        },
        deleteAlbum({ commit }, albumId) {
            album_service.deleteAlbum(albumId);
        }
    }
}