<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="classes"
      sort-by="calories"
      class="elevation-1"
    >
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
        educator: { name: 'Antonina Czajkowska', surname: 'elo' },
      },
      {
        id: 2,
        name: '3 c',
        students: 33,
        educator: { name: 'Antoni Król', surname: 'elo' },
      },
      {
        id: 3,
        name: '2 b',
        students: 22,
        educator: { name: 'Krzysztof Ibisz', surname: 'elo' },
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
  },
}
</script>
