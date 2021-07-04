<template>
  <div
    class="login form d-flex align-center justify-center flex-column"
    id="login"
  >
    <h1>Logowanie</h1>
    <v-col class="12 flex-grow-0">
      <v-form
        ref="form"
        class="d-flex flex-column"
        @submit.prevent="handleLogin"
      >
        <v-col cols="12">
          <v-text-field
            filled
            id="loginUsername"
            v-model="login.username"
            :rules="inputRules"
            label="Nazwa użytkownika"
            required
          ></v-text-field>
        </v-col>

        <v-col cols="12">
          <v-text-field
            filled
            id="loginPassword"
            v-model="login.password"
            :rules="inputRules"
            label="Hasło"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" class="d-flex justify-center">
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
  </div>
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
  mounted() {
    this.$axios.setHeader('Content-Type', 'application/x-www-form-urlencoded', [
      'post',
    ])
  },
}
</script>
<style scoped>
#login {
  height: 100%;
}
</style>
