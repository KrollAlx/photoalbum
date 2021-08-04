<template>    
    <v-card @click="$router.push('/album/' + album.id)">            
        <v-img height="200" :src="album.image"/>
        <v-card-title>Название: {{album.title}}</v-card-title>
        <v-card-text class="ml-3"> 
            <h4>Лайков: {{album.likes}}</h4>
            <h4>Комментариев: {{album.comments}}</h4>
            <h4>Владелец: {{album.owner}}</h4>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    props: {
        album: {
            required: true,
            type: Object
        }
    }
}
</script>