<template>
  <div>
    <v-alert border="left" color="deep-purple accent-4" dark>
      Podstrona pozwala na obsługę uczniów. Możesz edytować informacje o
      uczniach, dopisywać do klas.
    </v-alert>
    <div class="my-2">
      <v-btn color="info" to="/principal/users/new" dark large>
        Dodaj nowego ucznia
      </v-btn>
    </div>
    <v-data-table
      :headers="headers"
      :items="students"
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
    students: [{ id: 1, name: 'Andrzej', surname: 'Srandrzej', class: '5 a' }],
    headers: [
      {
        text: 'ID',
        align: 'start',
        sortable: false,
        value: 'id',
      },
      { text: 'Imie', value: 'name' },
      { text: 'Nazwisko', value: 'surname' },
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
        this.students = [...a, ...this.students]
      })
    },
    ...mapActions({
      getStudents: 'students/getStudents',
      deleteStudent: 'students/deleteStudent',
    }),

    editItem(item) {
      this.$router.push(`/principal/users/${item.id}`)
    },

    deleteItem(item) {
      this.deleteStudent(item.id).then((res) => {
        this.initialData()
      })
    },
  },
}
</script>
