<template>
  <div>
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
            <div class="pa-2 text-truncate">
              <nuxt-link
                :to="{
                  path: `subjects/${event.name}`,
                  query: {
                    subject: event.subjectId,
                    teacher: event.teacherId,
                  },
                }"
              >
                <span class="body-1 font-weight-bold">{{ event.name }}</span>
                <br />
                {{ event.teacher }}
                <br />
                <v-row align="center" class="ma-0">
                  <v-icon small dark class="mr-2"
                    >mdi-clock-time-four-outline</v-icon
                  >
                  {{ event.start | formatDateHour }} :
                  {{ event.end | formatDateHour }}
                </v-row>
              </nuxt-link>
            </div>
          </template>
          <template v-else>
            <div class="pa-1 text-truncate">
              <span class="caption font-weight-bold">{{ event.name }}</span>
              <!-- <br /> -->
              <!-- {{ event.teacher }} -->
            </div>
          </template>
        </template>
      </v-calendar>
    </v-sheet>
  </div>
</template>
<script>
export default {
  data: () => ({
    type: 'month',
    types: ['month', 'week', 'day'],
    weekday: [0, 1, 2, 3, 4, 5, 6],
    weekdays: [
      { text: 'Sun - Sat', value: [0, 1, 2, 3, 4, 5, 6] },
      { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
    ],
    value: '',
    events: [],
    colors: [
      'blue',
      'indigo',
      'deep-purple',
      'cyan',
      'green',
      'orange',
      'grey darken-1',
    ],
    names: [
      'Polski',
      'Angielski',
      'WF',
      'Przysposobienie obronne',
      'Edukacja wczesnoszkolna',
      'Matematyka',
      'Włoski',
      'Muzyka',
    ],
  }),
  mounted() {
    console.log(this.$router.getRoutes())
    this.events = [
      {
        name: 'Matematyka',
        start: new Date('2021-06-24T10:30:00.000Z'),
        end: new Date('2021-06-24T12:15:00.000Z'),
        color: 'grey darken-1',
        timed: true,
        teacher: 'Antonina 3',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Włoski',
        start: new Date('2021-06-07T23:30:00.000Z'),
        end: new Date('2021-06-08T00:00:00.000Z'),
        color: 'orange',
        timed: true,
        teacher: 'Antonina 1',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Edukacja wczesnoszkolna',
        start: new Date('2021-06-07T03:00:00.000Z'),
        end: new Date('2021-06-07T03:30:00.000Z'),
        color: 'indigo',
        timed: true,
        teacher: 'Antonina 6',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Muzyka',
        start: new Date('2021-06-18T12:00:00.000Z'),
        end: new Date('2021-06-18T13:30:00.000Z'),
        color: 'blue',
        timed: true,
        teacher: 'Antonina 3',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-18T17:30:00.000Z'),
        end: new Date('2021-06-18T19:30:00.000Z'),
        color: 'orange',
        timed: true,
        teacher: 'Antonina 8',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Matematyka',
        start: new Date('2021-06-13T16:00:00.000Z'),
        end: new Date('2021-06-13T17:15:00.000Z'),
        color: 'grey darken-1',
        timed: true,
        teacher: 'Antonina 2',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Matematyka',
        start: new Date('2021-06-19T20:15:00.000Z'),
        end: new Date('2021-06-19T21:30:00.000Z'),
        color: 'deep-purple',
        timed: true,
        teacher: 'Antonina 2',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Edukacja wczesnoszkolna',
        start: new Date('2021-06-16T11:15:00.000Z'),
        end: new Date('2021-06-16T12:00:00.000Z'),
        color: 'cyan',
        timed: true,
        teacher: 'Antonina 0',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'WF',
        start: new Date('2021-06-07T06:30:00.000Z'),
        end: new Date('2021-06-07T07:15:00.000Z'),
        color: 'deep-purple',
        timed: true,
        teacher: 'Antonina 0',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-23T10:30:00.000Z'),
        end: new Date('2021-06-23T12:30:00.000Z'),
        color: 'deep-purple',
        timed: true,
        teacher: 'Antonina 0',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Angielski',
        start: new Date('2021-06-21T02:00:00.000Z'),
        end: new Date('2021-06-21T03:30:00.000Z'),
        color: 'grey darken-1',
        timed: true,
        teacher: 'Antonina 5',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Matematyka',
        start: new Date('2021-06-26T22:45:00.000Z'),
        end: new Date('2021-06-27T00:30:00.000Z'),
        color: 'orange',
        timed: true,
        teacher: 'Antonina 8',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-02T02:15:00.000Z'),
        end: new Date('2021-06-02T03:00:00.000Z'),
        color: 'blue',
        timed: true,
        teacher: 'Antonina 3',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Edukacja wczesnoszkolna',
        start: new Date('2021-06-27T15:30:00.000Z'),
        end: new Date('2021-06-27T16:00:00.000Z'),
        color: 'blue',
        timed: true,
        teacher: 'Antonina 4',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Matematyka',
        start: new Date('2021-06-21T06:00:00.000Z'),
        end: new Date('2021-06-21T06:30:00.000Z'),
        color: 'indigo',
        timed: true,
        teacher: 'Antonina 5',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-24T06:00:00.000Z'),
        end: new Date('2021-06-24T07:30:00.000Z'),
        color: 'cyan',
        timed: true,
        teacher: 'Antonina 5',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Edukacja wczesnoszkolna',
        start: new Date('2021-06-19T03:45:00.000Z'),
        end: new Date('2021-06-19T05:00:00.000Z'),
        color: 'cyan',
        timed: true,
        teacher: 'Antonina 5',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'WF',
        start: new Date('2021-06-03T08:00:00.000Z'),
        end: new Date('2021-06-03T09:15:00.000Z'),
        color: 'cyan',
        timed: true,
        teacher: 'Antonina 6',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Matematyka',
        start: new Date('2021-06-16T23:45:00.000Z'),
        end: new Date('2021-06-17T01:30:00.000Z'),
        color: 'deep-purple',
        timed: true,
        teacher: 'Antonina 1',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-05T19:00:00.000Z'),
        end: new Date('2021-06-05T20:00:00.000Z'),
        color: 'deep-purple',
        timed: true,
        teacher: 'Antonina 8',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-21T09:00:00.000Z'),
        end: new Date('2021-06-21T11:00:00.000Z'),
        color: 'indigo',
        timed: true,
        teacher: 'Antonina 5',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Edukacja wczesnoszkolna',
        start: new Date('2021-06-13T22:15:00.000Z'),
        end: new Date('2021-06-14T00:00:00.000Z'),
        color: 'deep-purple',
        timed: true,
        teacher: 'Antonina 1',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Przysposobienie obronne',
        start: new Date('2021-06-21T05:30:00.000Z'),
        end: new Date('2021-06-21T07:30:00.000Z'),
        color: 'grey darken-1',
        timed: true,
        teacher: 'Antonina 4',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Edukacja wczesnoszkolna',
        start: new Date('2021-06-24T13:15:00.000Z'),
        end: new Date('2021-06-24T13:45:00.000Z'),
        color: 'blue',
        timed: true,
        teacher: 'Antonina 6',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Włoski',
        start: new Date('2021-06-19T04:15:00.000Z'),
        end: new Date('2021-06-19T05:00:00.000Z'),
        color: 'green',
        timed: true,
        teacher: 'Antonina 6',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'WF',
        start: new Date('2021-06-21T14:15:00.000Z'),
        end: new Date('2021-06-21T16:00:00.000Z'),
        color: 'blue',
        timed: true,
        teacher: 'Antonina 1',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Włoski',
        start: new Date('2021-06-30T03:00:00.000Z'),
        end: new Date('2021-06-30T04:15:00.000Z'),
        color: 'orange',
        timed: true,
        teacher: 'Antonina 8',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Muzyka',
        start: new Date('2021-06-15T19:30:00.000Z'),
        end: new Date('2021-06-15T20:00:00.000Z'),
        color: 'green',
        timed: true,
        teacher: 'Antonina 6',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Angielski',
        start: new Date('2021-06-20T15:30:00.000Z'),
        end: new Date('2021-06-20T17:30:00.000Z'),
        color: 'indigo',
        timed: true,
        teacher: 'Antonina 3',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-08T00:30:00.000Z'),
        end: new Date('2021-06-08T02:00:00.000Z'),
        color: 'green',
        timed: true,
        teacher: 'Antonina 2',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Edukacja wczesnoszkolna',
        start: new Date('2021-06-22T23:45:00.000Z'),
        end: new Date('2021-06-23T01:00:00.000Z'),
        color: 'orange',
        timed: true,
        teacher: 'Antonina 8',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'WF',
        start: new Date('2021-06-15T16:45:00.000Z'),
        end: new Date('2021-06-15T17:15:00.000Z'),
        color: 'cyan',
        timed: true,
        teacher: 'Antonina 5',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-22T21:45:00.000Z'),
        end: new Date('2021-06-22T23:00:00.000Z'),
        color: 'cyan',
        timed: true,
        teacher: 'Antonina 1',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'WF',
        start: new Date('2021-06-22T03:00:00.000Z'),
        end: new Date('2021-06-22T03:45:00.000Z'),
        color: 'indigo',
        timed: true,
        teacher: 'Antonina 8',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Matematyka',
        start: new Date('2021-06-27T13:45:00.000Z'),
        end: new Date('2021-06-27T14:15:00.000Z'),
        color: 'deep-purple',
        timed: true,
        teacher: 'Antonina 2',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-14T10:45:00.000Z'),
        end: new Date('2021-06-14T12:00:00.000Z'),
        color: 'orange',
        timed: true,
        teacher: 'Antonina 5',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Angielski',
        start: new Date('2021-06-19T11:30:00.000Z'),
        end: new Date('2021-06-19T12:30:00.000Z'),
        color: 'grey darken-1',
        timed: true,
        teacher: 'Antonina 4',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Edukacja wczesnoszkolna',
        start: new Date('2021-06-17T01:15:00.000Z'),
        end: new Date('2021-06-17T03:15:00.000Z'),
        color: 'grey darken-1',
        timed: true,
        teacher: 'Antonina 4',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Angielski',
        start: new Date('2021-06-25T06:15:00.000Z'),
        end: new Date('2021-06-25T07:00:00.000Z'),
        color: 'grey darken-1',
        timed: true,
        teacher: 'Antonina 4',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Przysposobienie obronne',
        start: new Date('2021-06-24T11:30:00.000Z'),
        end: new Date('2021-06-24T12:00:00.000Z'),
        color: 'deep-purple',
        timed: true,
        teacher: 'Antonina 2',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Polski',
        start: new Date('2021-06-30T03:30:00.000Z'),
        end: new Date('2021-06-30T04:00:00.000Z'),
        color: 'indigo',
        timed: true,
        teacher: 'Antonina 2',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Angielski',
        start: new Date('2021-06-28T10:00:00.000Z'),
        end: new Date('2021-06-28T11:15:00.000Z'),
        color: 'cyan',
        timed: true,
        teacher: 'Antonina 2',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'WF',
        start: new Date('2021-06-21T04:00:00.000Z'),
        end: new Date('2021-06-21T05:15:00.000Z'),
        color: 'orange',
        timed: true,
        teacher: 'Antonina 7',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Angielski',
        start: new Date('2021-06-08T16:30:00.000Z'),
        end: new Date('2021-06-08T18:00:00.000Z'),
        color: 'cyan',
        timed: true,
        teacher: 'Antonina 0',
        subjectId: 2,
        teacherId: 123,
      },
    ]
  },
  methods: {
    getEvents({ start, end }) {
      //  getEvents DB
      const events = []

      const min = new Date(`${start.date}T00:00:00`)
      const max = new Date(`${end.date}T23:59:59`)
      const days = (max.getTime() - min.getTime()) / 86400000
      const eventCount = this.rnd(days, days + 20)

      for (let i = 0; i < eventCount; i++) {
        const allDay = false
        const firstTimestamp = this.rnd(min.getTime(), max.getTime())
        const first = new Date(firstTimestamp - (firstTimestamp % 900000))
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
        const second = new Date(first.getTime() + secondTimestamp)

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay,
          teacher: 'Antonina ' + this.rnd(0, 8),
        })
      }

      // this.events = events
    },
    getEventColor(event) {
      return event.color
    },
    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
    showMore({ date }) {
      this.value = date
      this.type = 'day'
    },
  },
}
</script>
