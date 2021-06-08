<template>
  <div class="pa-2 text-truncate">
    <nuxt-link
      class="text-decoration-none white--text"
      :to="{
        path: `subjects/${event.name}`,
        query: {
          subject: event.subjectId,
          teacher: event.teacherId,
        },
      }"
    >
      <span class="body-1 font-weight-bold">{{ event.name }}</span>
      <br />
      {{ event.teacher }}
      <template v-if="showHours">
        <br />
        <v-row align="center" class="ma-0">
          <v-icon small dark class="mr-2">mdi-clock-time-four-outline</v-icon>
          {{ event.start | formatDateHour }} :
          {{ event.end | formatDateHour }}
        </v-row></template
      >
    </nuxt-link>
  </div>
</template>
<script>
export default {
  props: {
    event: {
      required: true,
      type: Object,
    },
    showHours: {
      type: Boolean,
      required: false,
      default: true,
    },
  },
}
</script>
