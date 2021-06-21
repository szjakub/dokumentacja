<template>
  <v-form ref="form" @submit.prevent="handleLogin">
    <v-text-field
      id="loginUsername"
      v-model="login.username"
      :rules="inputRules"
      label="Nazwa użytkownika"
      required
    ></v-text-field>

    <v-text-field
      id="loginPassword"
      v-model="login.password"
      :rules="inputRules"
      label="Hasło"
      required
    ></v-text-field>

    <v-btn type="submit" color="success" class="mr-4" @click="submit">
      Zaloguj
    </v-btn>
  </v-form>
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
