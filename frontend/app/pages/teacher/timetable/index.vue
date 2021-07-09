<template>
  <section id="lessson-plan">
    <Callendar :events="events"></Callendar>
  </section>
</template>
<script>
import Callendar from '../../../components/calendar/index.vue'
export default {
  components: {
    Callendar,
  },
  data: () => ({
    events: [],
  }),
  mounted() {
    this.events = [
      {
        name: 'Kartkówka 1B',
        start: new Date('2021-06-24T10:30:00.000Z'),
        end: new Date('2021-06-24T12:15:00.000Z'),
        color: 'orange',
        timed: true,
        teacher: 'Antonina 3',
        subjectId: 2,
        teacherId: 123,
      },

      {
        name: 'Sprawdzian 1B',
        start: new Date('2021-06-18T17:30:00.000Z'),
        end: new Date('2021-06-18T19:30:00.000Z'),
        color: 'orange',
        timed: true,
        teacher: 'Antonina 8',
        subjectId: 2,
        teacherId: 123,
      },

      {
        name: 'Kartkówka 3C',
        start: new Date('2021-06-16T11:15:00.000Z'),
        end: new Date('2021-06-16T12:00:00.000Z'),
        color: 'cyan',
        timed: true,
        teacher: 'Antonina 0',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Kartkówka 2G',
        start: new Date('2021-06-07T06:30:00.000Z'),
        end: new Date('2021-06-07T07:15:00.000Z'),
        color: 'brown',
        timed: true,
        teacher: 'Antonina 0',
        subjectId: 2,
        teacherId: 123,
      },

      {
        name: 'Sprawdzian 2G',
        start: new Date('2021-06-21T14:15:00.000Z'),
        end: new Date('2021-06-21T16:00:00.000Z'),
        color: 'pink',
        timed: true,
        teacher: 'Antonina 1',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Kartkówka 3A',
        start: new Date('2021-06-21T04:00:00.000Z'),
        end: new Date('2021-06-21T05:15:00.000Z'),
        color: 'green',
        timed: true,
        teacher: 'Antonina 7',
        subjectId: 2,
        teacherId: 123,
      },
      {
        name: 'Sprawdzian 3A',
        start: new Date('2021-06-08T16:30:00.000Z'),
        end: new Date('2021-06-08T18:00:00.000Z'),
        color: 'green',
        timed: true,
        teacher: 'Antonina 0',
        subjectId: 2,
        teacherId: 123,
      },
    ]
  },
}
</script>
