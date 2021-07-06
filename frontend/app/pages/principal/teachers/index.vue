<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="teachers"
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
    teachers: [
      { id: 1, name: 'Antonina', surname: 'Elo', class: '5 a', title: 'mgr' },
    ],
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
      { text: 'Tytuł', value: 'title' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
  }),

  created() {
    this.initialData()
  },

  methods: {
    initialData() {
      this.getTeachers().then((a) => {
        this.teachers = [...a, ...this.teachers]
      })
    },
    ...mapActions({
      getTeachers: 'teachers/getTeachers',
      deleteTeacher: 'teachers/deleteTeacher',
    }),

    editItem(item) {
      this.$router.push(`/principal/teachers/${item.id}`)
    },

    deleteItem(item) {
      this.deleteTeacher(item.id).then((res) => {
        this.initialData()
      })
    },
  },
}
</script>
