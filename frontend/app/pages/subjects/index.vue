<template>
  <div>
    <v-list subheader three-line>
      <template v-for="(subject, i) in subjects">
        <v-list-item
          :key="i"
          nuxt
          :to="{
            path: `subjects/${subject.name}`,
            query: { subject: subject.subjectId, teacher: subject.teacherId },
          }"
        >
          <v-list-item-content>
            <v-list-item-title>{{ subject.name }}</v-list-item-title>
            <v-list-item-subtitle>{{ subject.teacher }}</v-list-item-subtitle>
          </v-list-item-content>
          <v-list-item-action>
            <v-btn large icon>
              <v-icon color="grey lighten-1"
                >mdi-arrow-right-thin-circle-outline</v-icon
              >
            </v-btn>
          </v-list-item-action>
        </v-list-item>
        <v-divider
          v-if="i < subjects.length - 1"
          :key="`${i} - divider`"
        ></v-divider>
      </template>
    </v-list>
  </div>
</template>
<script>
export default {
  data() {
    return {
      subjects: [
        {
          name: 'Angielski',
          teacher: 'Alfona Ptak',
          subjectId: 1,
          teacherId: 123,
        },
        {
          name: 'Polski',
          teacher: 'Alfona Ptak',
          subjectId: 1,
          teacherId: 123,
        },
        {
          name: 'Muzyka',
          teacher: 'Alfona Ptak',
          subjectId: 1,
          teacherId: 123,
        },
      ],
    }
  },
  mounted() {
    console.log(this)
  },
}
</script>
