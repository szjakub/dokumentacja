<template>
  <v-card class="mx-auto" tile elevation="0">
    <v-navigation-drawer permanent width="300">
      <v-list>
        <v-list-item>
          <v-list-item-avatar class="mx-auto" size="100" rounded>
            <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="text-h6 text-center">
              Apoloniusz Jędrzejczyk
            </v-list-item-title>
            <v-list-item-subtitle
              ><v-chip class="ml-0 mr-2 black--text" label small> 3 A </v-chip>
              <v-chip class="ml-0 mr-2 black--text" label small>
                2020/2021
              </v-chip></v-list-item-subtitle
            >
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item-group v-model="selectedItem" color="primary">
          <v-list-item v-for="(item, i) in items" :key="i" :to="item.link" nuxt>
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>
<script>
export default {
  name: 'PanelNavigation',
  data: () => ({
    selectedItem: 0,
    items: [],
  }),
  created() {
    switch (this.$store.state.user.type) {
      case 'principal':
        this.items = [
          { text: 'Główna', icon: 'mdi-users', link: '/principal' },
          { text: 'Studenci', icon: 'mdi-users', link: '/principal/users' },
          {
            text: 'Nauczyciele',
            icon: 'mdi-users',
            link: '/principal/teachers',
          },
          { text: 'Klasy', icon: 'mdi-users', link: '/principal/classes' },
          {
            text: 'Przedmioty',
            icon: 'mdi-users',
            link: '/principal/subjects',
          },
        ]
        break
      case 'teacher':
        this.items = [
          { text: 'Studenci', icon: 'mdi-users', link: '/principal' },
        ]
        break
      case 'student':
        this.items = [
          { text: 'Mój Plan lekcji', icon: 'mdi-folder', link: '/plan-zajec' },
          {
            text: 'Panel obecności',
            icon: 'mdi-account-multiple',
            link: '/panel-obecnosci',
          },
          { text: 'Moje Oceny', icon: 'mdi-star', link: '/grades' },
          { text: 'Moje przedmioty', icon: 'mdi-history', link: '/subjects' },
          {
            text: 'Zadania domowe',
            icon: 'mdi-check-circle',
            link: '/homework',
          },
          {
            text: 'Sprawdziany i kartkówki',
            icon: 'mdi-upload',
            link: '/tests',
          },
          { text: 'Ogłoszenia', icon: 'mdi-cloud-upload', link: '/news' },
          { text: 'Moi nauczyciele', icon: 'mdi-cloud-upload', link: '' },
        ]
        // redirect('/student')
        break
    }
  },
}
</script>
