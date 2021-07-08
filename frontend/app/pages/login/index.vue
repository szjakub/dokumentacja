<template>
  <div
    class="login form d-flex align-center justify-center flex-column"
    id="login"
  >
    <h1>Logowanie</h1>
    <div class="errors" v-if="Object.keys(errors).length > 0">
      <v-alert type="error" v-for="(error, index) in errors" :key="index">
        {{ error[0] }}
      </v-alert>
    </div>
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
        <v-col cols="12">
          <v-select
            v-model="type"
            :items="typeOfUser"
            label="Typ użytkownika"
            filled
            persistent-hint
            item-text="name"
            required
            item-value="value"
          ></v-select>
        </v-col>
        <v-col cols="12" class="d-flex justify-center">
          <v-btn type="submit" color="success" class="mr-4" large>
            Zaloguj się
          </v-btn>
          <v-btn
            :to="'/registration'"
            type="submit"
            color="info"
            class="mr-4"
            large
          >
            Zarejestruj się
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
      type: null,
      typeOfUser: [
        { name: 'Moderator', value: 'principal' },
        { name: 'Nauczyciel', value: 'teacher' },
        { name: 'Uczeń', value: 'student' },
      ],
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
            this.setType(this.type)
            this.$router.push(this.type)
          })
          .catch((e) => {
            if (e.response) {
              this.errors = e.response.data
            } else {
              console.error(e.message)
            }
          })
      }
    },
    ...mapMutations({
      setToken: 'user/SET_TOKEN',
      setType: 'user/SET_TYPE_USER',
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
