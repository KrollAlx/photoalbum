<template>
    <span>
        <v-btn color="light-green" class="mr-3"
            @click="$router.push('/albums?popular=false')">
            Мои альбомы
        </v-btn>

        <v-btn color="light-green"
            @click="$router.push('/albums?popular=true')">
            Популярные альбомы
        </v-btn>
    </span>
</template>