<template>
  <section>
    <v-row>
      <v-col>
        <HeaderPage></HeaderPage>
        <nuxt-link
          to="/techer"
          class="techer-name text-subtitle-1 text-black text-decoration-none"
          >Aldona Ptak</nuxt-link
        >
      </v-col>
    </v-row>
    <v-row>
      <v-col md="4">
        <v-card>
          <v-card-title>
            <h3 class="subtitle-1">
              Twoje ostatnie oceny z przedmiotu:
              <strong>{{ $route.params.slug }}</strong>
            </h3>
          </v-card-title>
          <v-card-text>
            <v-list>
              <!-- <v-subheader>Ostatnie oceny</v-subheader> -->
              <v-list-item-group color="primary">
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      <v-chip
                        label
                        class="mr-2"
                        color="green"
                        text-color="white"
                      >
                        5
                      </v-chip>
                      Sprawdzian 20.10.2002
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      <v-chip label class="mr-2" color="red" text-color="white">
                        1
                      </v-chip>
                      Odpowiedź ustana 23456 8720.10.2002
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card-text>
          <v-card-actions>
            <v-btn nuxt to="/" text> Zobacz moje oceny </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col md="4">
        <v-card>
          <v-card-title>
            <h3 class="subtitle-1">
              Zbliżające się wydarzenia przedmiotu
              <strong>{{ $route.params.slug }}</strong>
            </h3>
          </v-card-title>
          <v-card-text>
            <v-list>
              <!-- <v-subheader>Ostatnie oceny</v-subheader> -->
              <v-list-item-group color="primary">
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      <v-chip
                        label
                        class="mr-2"
                        color="blue"
                        text-color="white"
                      >
                        20.10.2002
                      </v-chip>
                      Sprawdzian dział 5
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>
                      <v-chip
                        label
                        class="mr-2"
                        color="blue"
                        text-color="white"
                      >
                        21.08.2020
                      </v-chip>
                      Odpowiedź ustana 23456 87
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card-text>
          <v-card-actions>
            <v-btn nuxt to="/" text> Zobacz mój kalendarz </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col md="4">
        <v-card>
          <v-card-title>
            <h3 class="subtitle-1">
              Najbliższa lekcja:
              <strong>{{ $route.params.slug }}</strong>
            </h3>
          </v-card-title>
          <v-card-text>
            <p class="text-h4 text-center">07.06.2020</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </section>
</template>
<script>
import HeaderPage from '../../../components/pages/HeaderPage.vue'
export default {
  components: {
    HeaderPage,
  },
  data: () => ({
    reveal: false,
  }),
  mounted() {
    console.log(this.$store)
  },
}
</script>
