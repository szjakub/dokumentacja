<template>
  <div id="callendar-wrapper">
    <v-sheet tile height="54" class="d-flex">
      <v-btn icon class="ma-2" @click="$refs.calendar.prev()">
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
      <v-select
        v-model="type"
        :items="types"
        dense
        outlined
        hide-details
        class="ma-2"
        label="type"
      ></v-select>
      <v-select
        v-model="weekday"
        :items="weekdays"
        dense
        outlined
        hide-details
        label="weekdays"
        class="ma-2"
      ></v-select>
      <v-spacer></v-spacer>
      <v-btn icon class="ma-2" @click="$refs.calendar.next()">
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </v-sheet>
    <v-sheet height="700">
      <v-calendar
        ref="calendar"
        v-model="value"
        :weekdays="weekday"
        :type="type"
        :events="events"
        :event-overlap-threshold="30"
        :interval-count="12"
        :event-height="type == 'day' ? 80 : 30"
        :first-interval="7"
        :event-color="getEventColor"
        @change="getEvents"
        @click:more="showMore"
        @click:date="showMore"
      >
        <template v-slot:event="{ event }">
          <template v-if="type == 'day'">
            <template v-if="presence">
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <EventDay :show-hours="showHours" :event="event"></EventDay>
                  </div>
                </template>
                <span>{{
                  event.presence
                    ? event.delayed
                      ? 'Spóźniony'
                      : 'Obecny'
                    : 'Nieobecny'
                }}</span>
              </v-tooltip>
            </template>
            <template v-else>
              <EventDay :show-hours="showHours" :event="event"></EventDay>
            </template>
          </template>
          <template v-else>
            <template v-if="presence">
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <div v-bind="attrs" v-on="on">
                    <EventDefault :event="event"></EventDefault>
                  </div>
                </template>
                <span>{{
                  event.presence
                    ? event.delayed
                      ? 'Spóźniony'
                      : 'Obecny'
                    : 'Nieobecny'
                }}</span>
              </v-tooltip>
            </template>
            <template v-else>
              <EventDefault :event="event"></EventDefault>
            </template>
          </template>
        </template>
      </v-calendar>
    </v-sheet>
    <v-row v-if="presenceLegend" class="mt-8">
      <v-card class="mx-auto" width="100%" outlined>
        <v-list-item>
          <v-list-item-content>
            <div class="text-overline text-uppercase">Legenda</div>
          </v-list-item-content>
        </v-list-item>

        <v-card-actions>
          <v-chip class="mx-2" text-color="white" color="red" label>
            Nieobecny
          </v-chip>
          <v-chip class="mx-2" text-color="white" color="yellow" label>
            Spóźniony
          </v-chip>
          <v-chip class="mx2" text-color="white" color="green" label>
            Obecny
          </v-chip>
        </v-card-actions>
      </v-card>
    </v-row>
  </div>
</template>
<script>
import EventDay from './EventDay.vue'
import EventDefault from './EventDefault.vue'
export default {
  components: {
    EventDay,
    EventDefault,
  },
  props: {
    events: {
      type: Array,
      required: true,
    },
    showHours: {
      type: Boolean,
      required: false,
      default: true,
    },
    presence: {
      type: Boolean,
      required: false,
      default: false,
    },
    presenceLegend: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data: () => ({
    type: 'month',
    types: ['month', 'week', 'day'],
    weekday: [0, 1, 2, 3, 4, 5, 6],
    weekdays: [
      { text: 'Sun - Sat', value: [0, 1, 2, 3, 4, 5, 6] },
      { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
    ],
    value: '',
  }),
  methods: {
    getEvents() {
      // action get next day/ montt axios
    },
    showMore({ date }) {
      this.value = date
      this.type = 'day'
    },
    getEventColor(event) {
      if (this.presence) {
        if (event.presence) {
          if (event.delayed) {
            return 'yellow'
          }
          return 'green'
        } else {
          return 'red'
        }
      } else {
        return event.color
      }
    },
  },
}
</script>
