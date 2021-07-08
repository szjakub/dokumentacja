<template>
  <div
    class="registration form d-flex align-center justify-center flex-column"
    id="registration"
  >
    <h1>Rejestracja szkoły</h1>
    {{ errors }}
    <v-col class="12 flex-grow-0">
      <v-form
        ref="form"
        class="d-flex flex-column"
        @submit.prevent="handleRegistration"
      >
        <v-col cols="12">
          <v-text-field
            filled
            v-model="registration.user.email"
            :rules="inputRules"
            label="E-mail"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-text-field
            filled
            v-model="registration.user.first_name"
            :rules="inputRules"
            label="Imię"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-text-field
            filled
            v-model="registration.user.last_name"
            :rules="inputRules"
            label="Nazwisko"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-text-field
            filled
            v-model="registration.school.school_name"
            :rules="inputRules"
            label="Nazwa szkoły"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-text-field
            filled
            v-model="registration.school.school_address"
            :rules="inputRules"
            label="Adres szkoły"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" class="d-flex justify-center">
          <v-btn type="submit" color="success" class="mr-4" large>
            Rejestracja
          </v-btn>
          <v-btn :to="'/login'" type="submit" color="info" class="mr-4" large>
            Zaloguj się
          </v-btn>
        </v-col>
      </v-form>
    </v-col>
  </div>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  layout: 'login',
  data() {
    return {
      registration: {
        user: {
          email: 'a',
          first_name: 'a',
          last_name: 'a',
        },
        school: {
          school_name: 'a',
          school_address: 'a',
        },
      },
      errors: {},
      inputRules: [(v) => !!v || 'Pole nie może byc puste'],
    }
  },
  methods: {
    ...mapActions({
      schoolRegister: 'user/schoolRegister',
    }),

    handleRegistration(e) {
      this.schoolRegister(this.registration)
        .then((e) => {
          this.$router.push('login')
        })
        .catch((e) => {
          this.errors = e.response.data
        })
    },
  },
}
</script>
<style scoped>
#registration {
  height: 100%;
}
</style>
