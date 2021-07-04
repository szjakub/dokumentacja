<template>
  <v-app dark>
    <v-row>
      <v-col cols="6" class="py-0">
        <v-img height="100%" position="left center" src="/main.jpg"> </v-img>
      </v-col>
      <v-col cols="6" class="py-0">
        <nuxt />
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
export default {
  layout: 'login',
  props: {},
  data() {
    return {}
  },
}
</script>

<style scoped></style>
