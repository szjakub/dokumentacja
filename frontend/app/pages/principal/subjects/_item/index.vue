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
          v-model="subjectObj.name"
          :rules="inputRules"
          label="Nazwa przedmiotu"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-select
          v-model="subjectObj.teachers"
          :items="teachersList"
          :menu-props="{ maxHeight: '400' }"
          label="Nauczyciele"
          multiple
          filled
          persistent-hint
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
      subjectObj: {
        name: '',
        teachers: [],
      },
      teachersList: [1, 2, 3, 4, 5, 6],
      id: 1,
      errors: {},
      inputRules: [(v) => v.length > 0 || 'Pole nie może byc puste'],
    }
  },
  created() {
    this.getSubject(this.id).then((res) => {
      this.subjectObj = res
    })
  },
  methods: {
    handleEditUser(e) {
      if (this.$refs.form.validate()) {
        this.updateSubject({ ...this.subjectObj, ...{ id: this.id } }).then(
          (e) => {
            this.$router.push(`/principal/subjects`)
          }
        )
      }
    },
    ...mapActions({
      updateSubject: 'subjects/updateSubject',
      getSubject: 'subjects/getSubject',
    }),
  },
}
</script>
