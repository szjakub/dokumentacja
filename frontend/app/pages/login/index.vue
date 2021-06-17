<template>
  <v-col cols="12" md="12" class="d-flex justify-center flex-column">
    <v-col
      cols="12"
      md="12"
      class="d-flex justify-center align-center flex-column"
    >
      <h2>Logowanie</h2>
    </v-col>
    <v-form
      ref="form"
      class="d-flex align-center flex-column"
      @submit.prevent="handleLogin"
    >
      <v-col cols="12" md="4">
        <v-text-field
          id="loginUsername"
          v-model="login.username"
          :rules="inputRules"
          label="Nazwa użytkownika"
          required
        ></v-text-field>
      </v-col>

      <v-col cols="12" md="4">
        <v-text-field
          id="loginPassword"
          v-model="login.password"
          :rules="inputRules"
          label="Hasło"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="4" class="d-flex justify-center">
        <v-btn
          type="submit"
          color="success"
          class="mr-4 rounded-xl"
          @click="submit"
        >
          Zaloguj się
        </v-btn>
      </v-col>
    </v-form>
  </v-col>
</template>

<script>
export default {
  layout: 'login',
  data() {
    return {
      login: {
        username: '',
        password: '',
      },
      inputRules: [(v) => v.length > 0 || 'Pole nie może byc puste'],
    }
  },
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        this.handleLogin()
      }
    },
    handleLogin(e) {
      const Login = this.login.username
      const Password = this.login.password
      if (Login && Password) {
        console.log(Login, Password)
      } else console.log('puste')
    },
  },
}
</script>
