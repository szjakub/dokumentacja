<template>
  <div>
    <v-form
      ref="form"
      class="d-flex flex-column"
      @submit.prevent="handleEditTeacher"
    >
      <v-col cols="12">
        <v-text-field
          filled
          v-model="teacher.name"
          :rules="inputRules"
          label="Imię"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-text-field
          filled
          v-model="teacher.surname"
          :rules="inputRules"
          label="Nazwisko"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-select
          filled
          v-model="teacher.class"
          :rules="inputRules"
          label="Klasa"
          :items="['1a', '2b']"
          required
        ></v-select>
      </v-col>
      <v-col cols="12">
        <v-text-field
          filled
          v-model="teacher.title"
          :rules="inputRules"
          label="Tytuł"
          required
        ></v-text-field>
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
  name: 'editTeacher',
  data() {
    return {
      teacher: {
        name: '',
        surname: '',
        class: '',
        title: '',
      },
      id: 1,
      errors: {},
      inputRules: [(v) => v.length > 0 || 'Pole nie może byc puste'],
    }
  },
  created() {
    this.getTeacher(this.id).then((res) => {
      this.teacher = res
    })
  },
  methods: {
    handleEditTeacher(e) {
      if (this.$refs.form.validate()) {
        this.updateTeacher({ ...this.teacher, ...{ id: this.id } }).then(
          (e) => {
            this.$router.push(`/principal/teachers`)
          }
        )
      }
    },
    ...mapActions({
      updateTeacher: 'teachers/updateTeacher',
      getTeacher: 'teachers/getTeacher',
    }),
  },
}
</script>
