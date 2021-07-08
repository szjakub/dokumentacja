<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="classes"
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
    classes: [
      {
        id: 1,
        name: '5 a',
        students: 39,
        educator: { name: 'antonina', surname: 'elo' },
      },
    ],
    headers: [
      {
        text: 'ID',
        align: 'start',
        sortable: false,
        value: 'id',
      },
      { text: 'Klas', value: 'name' },
      { text: 'Ilość uczniów', value: 'students' },
      { text: 'Wychowawca', value: 'educator.name' },
      { text: 'Actions', value: 'actions', sortable: false },
    ],
  }),

  created() {
    this.initialData()
  },

  methods: {
    initialData() {
      this.getClasses().then((a) => {
        this.classes = [...a, ...this.classes]
      })
    },
    ...mapActions({
      getClasses: 'classes/getClasses',
      deleteClass: 'classes/deleteClass',
    }),

    editItem(item) {
      this.$router.push(`/principal/classes/${item.id}`)
    },

    deleteItem(item) {
      this.deleteClass(item.id).then((res) => {
        this.initialData()
      })
    },
  },
}
</script>
