<template>
  <v-row>
    <v-col md="8">
      <v-timeline dense clipped>
        <v-slide-x-transition group>
          <v-timeline-item
            v-for="event in timeline"
            :key="event.id"
            class="mb-4"
            color="pink"
            small
          >
            <v-row justify="space-between">
              <v-col
                cols="7"
                class="font-weight-bold"
                v-text="event.text"
              ></v-col>
              <v-col class="text-right" cols="5" v-text="event.time"></v-col>
              <v-col
                v-if="
                  event.shortDescription && event.shortDescription.length > 0
                "
                cols="12"
                class="text-left subtitle-1"
              >
                <div
                  class="text-left subtitle-1"
                  v-text="event.shortDescription"
                ></div>
                <div class="read-more">
                  <v-btn color="secondary" @click="showMore(event)">
                    Read more
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </v-timeline-item>
        </v-slide-x-transition>
      </v-timeline>
    </v-col>
    <v-col md="4">
      <v-card
        class="mx-auto"
        max-width="344"
        outlined
        v-if="showMoreEvent != null"
      >
        <v-list-item three-line>
          <v-list-item-content>
            <div class="text-overline mb-4">WIECEJ INFORMACJI</div>
            <v-list-item-title class="text-h5 mb-1">
              {{ showMoreEvent.text }}
            </v-list-item-title>

            <v-list-item-subtitle>{{
              showMoreEvent.shortDescription
            }}</v-list-item-subtitle>
            <v-chip-group
              active-class="deep-purple accent-4 white--text"
              column
            >
              <v-chip color="primary">
                {{ showMoreEvent.time }}
              </v-chip>
            </v-chip-group>
          </v-list-item-content>
        </v-list-item>
      </v-card>
    </v-col>
  </v-row>
</template>
<script>
export default {
  data: () => ({
    events: [
      {
        id: 2,
        text: ' Wycieczka 2020',
        time: '02-20-2020',
        shortDescription:
          'Wycieczka 2020 bediz eorganizowana dla całej szkoły i ucznia Zapsramy',
      },
      { id: 1, text: ' Zadanie dla całej szkoły', time: '02-20-2021' },
    ],
    showMoreEvent: null,
  }),

  computed: {
    timeline() {
      return this.events.slice().reverse()
    },
  },

  methods: {
    showMore(event) {
      this.showMoreEvent = event
    },
  },
  mounted() {
    console.log(this.$router.getRoutes())
  },
}
</script>
