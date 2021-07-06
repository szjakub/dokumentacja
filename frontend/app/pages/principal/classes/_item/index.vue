<template>
  <div>
    <v-form
      ref="form"
      class="d-flex flex-column"
      @submit.prevent="handleEditUser"
    >
      <v-col cols="12">
        <v-text-field
          filled
          v-model="classObj.name"
          :rules="inputRules"
          label="Nazwa klasy"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-select
          v-model="classObj.students"
          :items="studentsList"
          :menu-props="{ maxHeight: '400' }"
          label="Uczniowie"
          multiple
          filled
          persistent-hint
        ></v-select>
      </v-col>
      <v-col cols="12">
        <v-select
          filled
          v-model="classObj.teacher"
          :rules="inputRules"
          label="Klasa"
          :items="['1 nauczyciel', '2 nauczyciel']"
          required
        ></v-select>
      </v-col>

      <v-col cols="12" class="d-flex justify-center">
        <v-btn type="submit" color="success" class="mr-4 rounded-xl">
          Zaktualizuj
        </v-btn>
      </v-col>
    </v-form>
  </div>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  name: 'editClasses',
  data() {
    return {
      classObj: {
        name: '',
        students: [],
        teacher: 1,
      },
      studentsList: [1, 2, 3, 4, 5, 6],
      id: 1,
      errors: {},
      inputRules: [(v) => v.length > 0 || 'Pole nie może byc puste'],
    }
  },
  created() {
    this.getClass(this.id).then((res) => {
      this.classObj = res
    })
  },
  methods: {
    handleEditUser(e) {
      if (this.$refs.form.validate()) {
        this.updateClass({ ...this.classObj, ...{ id: this.id } }).then((e) => {
          this.$router.push(`/principal/classes`)
        })
      }
    },
    ...mapActions({
      updateClass: 'classes/updateClass',
      getClass: 'classes/getClass',
    }),
  },
}
</script>
