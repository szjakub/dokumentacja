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
          v-model="user.name"
          :rules="inputRules"
          label="Imię"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-text-field
          filled
          v-model="user.surname"
          :rules="inputRules"
          label="Nazwisko"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12">
        <v-select
          filled
          v-model="user.class"
          :rules="inputRules"
          label="Klasa"
          :items="['Foo', 'Bar']"
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
      user: {
        name: '',
        surname: '',
        class: '',
      },
      id: 1,
      errors: {},
      inputRules: [(v) => v.length > 0 || 'Pole nie może byc puste'],
    }
  },
  created() {
    this.getStudent(this.id).then((res) => {
      this.user = res
    })
  },
  methods: {
    handleEditUser(e) {
      if (this.$refs.form.validate()) {
        this.updateStudent({ ...this.user, ...{ id: this.id } }).then((e) => {
          this.$router.push(`/principal/users`)
        })
      }
    },
    ...mapActions({
      updateStudent: 'students/updateStudent',
      getStudent: 'students/getStudent',
    }),
  },
}
</script>
