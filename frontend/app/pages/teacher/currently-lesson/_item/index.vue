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
          v-model="currentlyLesson.subject"
          :rules="inputRules"
          label="Przedmiot"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-text-field
          filled
          v-model="currentlyLesson.topic"
          :rules="inputRules"
          label="Temat lekcji"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-select
          filled
          v-model="currentlyLesson.class"
          :rules="inputRules"
          label="Klasa"
          :items="['5a', '5b']"
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
  name: 'editUser',
  data() {
    return {
      currentlyLesson: {
        subject: 'Polski',
        topic: '',
        class: '',
      },
      id: 1,
      errors: {},
      inputRules: [(v) => v.length > 0 || 'Pole nie może byc puste'],
    }
  },
  created() {
    if (
      this.$router.currentRoute.params &&
      this.$router.currentRoute.params.item !== 'new'
    ) {
      this.getStudent(this.id).then((res) => {
        this.user = res
      })
    }
  },
  methods: {
    handleEditUser(e) {
      if (this.$refs.form.validate()) {
        this.updateStudent({
          ...this.currentlyLesson,
          ...{ id: this.id },
        }).then((e) => {
          this.$router.push(`/teacher/currently-lesson`)
        })
      }
    },
    ...mapActions({
      updateStudent: 'teacher/updateStudent',
      getStudent: 'students/getStudent',
    }),
  },
}
</script>
