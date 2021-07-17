<template>
  <div>
    <div class="my-2">
      <v-btn color="info" to="/teacher/currently-lesson/new" dark large>
        Dodaj temat lekcji
      </v-btn>
    </div>
    <v-data-table
      :headers="headers"
      :items="lessons"
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
  name: 'userList',
  data: () => ({
    lessons: [{ id: 1, subject: 'Polski', topic: 'Lalka', class: '5 a' }],
    headers: [
      {
        text: 'ID',
        align: 'start',
        sortable: false,
        value: 'id',
      },
      { text: 'Przedmiot', value: 'subject' },
      { text: 'Temat lekcji', value: 'topic' },
      { text: 'Klasa', value: 'class' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
  }),

  created() {
    this.initialData()
  },

  methods: {
    initialData() {
      this.getStudents().then((a) => {
        this.lessons = [...a, ...this.lessons]
      })
    },
    ...mapActions({
      getStudents: 'students/getStudents',
      deleteStudent: 'students/deleteStudent',
    }),

    editItem(item) {
      this.$router.push(`/teacher/currently-lesson/${item.id}`)
    },

    deleteItem(item) {
      this.deleteStudent(item.id).then((res) => {
        this.initialData()
      })
    },
  },
}
</script>
