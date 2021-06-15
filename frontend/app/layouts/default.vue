<template>
  <v-app dark>
    <v-app-bar fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title v-text="title" />
      <v-spacer />
    </v-app-bar>
    <v-main>
      <v-container>
        <v-row align-content="space-between">
          <transition name="slide-x-transition">
            <v-col v-show="drawer" cols="12" md="3" lg="3">
              <panel-navigation></panel-navigation>
            </v-col>
          </transition>
          {{ gettersIP }}
          <transition name="slide-x-transition">
            <v-col
              v-show="(drawer && !columnRouter) || (!drawer && columnRouter)"
              cols="12"
              :md="columnRouter ? 12 : 9"
            >
              <nuxt />
            </v-col>
          </transition>
        </v-row>
      </v-container>
    </v-main>
    <v-footer app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import PanelNavigation from '~/components/user/panels/PanelNavigation.vue'

export default {
  components: {
    'panel-navigation': PanelNavigation,
  },
  data() {
    return {
      drawer: true,
      columnRouter: false,
      title: 'Cyprus',
    }
  },
  computed: {
    ...mapGetters({
      gettersIP: 'user/gettersIP',
    }),
  },
  watch: {
    drawer() {
      setTimeout(() => {
        this.columnRouter = !this.columnRouter
      }, 360)
    },
  },
  mounted() {
    console.log(this)
    // console.log(this)
  },
  methods: {
    ...mapActions({ getIP: 'user/actions' }),
  },
}
</script>
