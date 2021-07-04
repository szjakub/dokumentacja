<template>
  <div
    class="login form d-flex align-center justify-center flex-column"
    id="login"
  >
    <h1>Logowanie</h1>
    {{ errors }}
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
          <v-btn type="submit" color="success" class="mr-4 rounded-xl">
            Zaloguj się
          </v-btn>
        </v-col>
      </v-form>
    </v-col>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'

export default {
  layout: 'login',
  data() {
    return {
      login: {
        username: '',
        password: '',
      },
      errors: {},
      inputRules: [(v) => v.length > 0 || 'Pole nie może byc puste'],
    }
  },
  methods: {
    handleLogin(e) {
      if (this.$refs.form.validate()) {
        this.loginAction(this.login)
          .then((e) => {
            this.$axios.setToken(e.token, 'Token')
            this.setToken(e.token)
            this.$router.push('news')
            window.sessionStorage.setItem('token', e.token)
          })
          .catch((e) => {
            this.errors = e.response.data
          })
      }
    },
    ...mapMutations({
      setToken: 'user/SET_TOKEN',
    }),
    ...mapActions({
      loginAction: 'user/login',
    }),
  },
}
</script>
<style scoped>
#login {
  height: 100%;
}
</style>
