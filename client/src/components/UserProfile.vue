<template>
  <span>
      <v-icon class="mr-3">mdi-account</v-icon>
      <span>{{ $store.getters['auth/getUsername'] }}</span>
  </span>
</template>