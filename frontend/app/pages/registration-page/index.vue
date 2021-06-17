<template>
  <v-col cols="12" md="12" class="d-flex justify-center flex-column">
    <v-col
      cols="12"
      md="12"
      class="d-flex justify-center align-center flex-column"
    >
      <h2>Rejestracja szkoły</h2>
    </v-col>

    <v-form
      ref="form"
      class="d-flex align-center flex-column"
      @submit.prevent="handleRegistration"
    >
      <v-col cols="12" md="4"
        ><v-text-field
          id="registrationEmail"
          v-model="registration.principalEmail"
          :rules="emailRules"
          label="Email"
          required
        ></v-text-field
      ></v-col>

      <v-col cols="12" md="4">
        <v-text-field
          id="schoolName"
          v-model="registration.schoolName"
          :rules="inputRules"
          label="Nazwa szkoły"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="4">
        <v-text-field
          id="schoolAddress"
          v-model="registration.schoolAddress"
          :rules="inputRules"
          label="Adres szkoły"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="4" class="d-flex justify-center">
        <v-btn
          type="submit"
          color="success"
          class="md-4 rounded-xl"
          @click="submit"
        >
          Rejestracja
        </v-btn>
      </v-col>
    </v-form>
  </v-col>
</template>
<script>
export default {
  layout: 'registration',
  data() {
    return {
      registration: {
        principalEmail: '',
        schoolName: '',
        schoolAddress: '',
      },
      inputRules: [(v) => !!v || 'Pole nie może byc puste'],
      emailRules: [
        (v) => v.length > 0 || 'Pole nie może być puste',
        (v) => /.+@.+\..+/.test(v) || 'Adres e-mail musi być poprawny',
      ],
    }
  },
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        this.handleRegistration()
      }
    },
    handleRegistration(e) {
      const email = this.registration.principalEmail
      const schoolName = this.registration.schoolName
      const schoolAddress = this.registration.schoolAddress
      if (this.$refs.form.validate()) {
        console.log(email, schoolName, schoolAddress)
      } else console.log('puste')
    },
  },
}
</script>
