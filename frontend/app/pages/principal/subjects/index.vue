<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="subjects"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
      </template>
    </v-data-table>
  </div>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  name: 'subjectsList',
  data: () => ({
    subjects: [
      {
        id: 1,
        name: 'Polski',
        teachers: 39,
      },
    ],
    headers: [
      {
        text: 'ID',
        align: 'start',
        sortable: false,
        value: 'id',
      },
      { text: 'Nazwa przemdiotu', value: 'name' },
      { text: 'Ilość nauczycieli', value: 'teachers' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
  }),

  created() {
    this.initialData()
  },

  methods: {
    initialData() {
      this.getSubjects().then((a) => {
        this.subjects = [...a, ...this.subjects]
      })
    },
    ...mapActions({
      getSubjects: 'subjects/getSubjects',
      deleteSubject: 'subjects/deleteSubject',
    }),

    editItem(item) {
      this.$router.push(`/principal/subjects/${item.id}`)
    },

    deleteItem(item) {
      this.deleteSubject(item.id).then((res) => {
        this.initialData()
      })
    },
  },
}
</script>
