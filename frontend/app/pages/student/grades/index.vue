<template>
  <section id="grades">
    <v-expansion-panels>
      <v-expansion-panel v-for="(subject, index) in grades" :key="index">
        <v-expansion-panel-header v-slot="{ open }">
          <v-row no-gutters>
            <v-col cols="4" class="text-h6 d-flex align-center">
              {{ subject.name }}
            </v-col>
            <v-col cols="8" class="text--secondary">
              <v-fade-transition leave-absolute>
                <!-- <span v-if="open" key="0"> Select trip destination </span> -->
                <span v-if="!open">
                  <template v-if="subject.grades.length >= 4">
                    <v-chip
                      v-for="grade in 3"
                      :key="grade"
                      label
                      class="ma-2"
                      :color="
                        subject.grades[grade].value >= 3 ? 'green' : 'red'
                      "
                      text-color="white"
                    >
                      {{ subject.grades[grade].value }}
                    </v-chip>
                  </template>
                  <template v-else>
                    <v-chip
                      v-for="(grade, i) in subject.grades"
                      :key="i"
                      label
                      class="ma-2"
                      :color="grade.value >= 3 ? 'green' : 'red'"
                      text-color="white"
                    >
                      <!-- {{ grade }} -->
                      {{ grade.value }}
                    </v-chip>
                  </template>
                  <template v-if="subject.grades.length >= 4">
                    <v-chip label class="ma-2" color="grey" text-color="white">
                      ...
                    </v-chip>
                  </template>
                </span>
              </v-fade-transition>
            </v-col>
          </v-row>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-list>
            <v-list-item-group color="primary">
              <v-list-item v-for="(grade, i) in subject.grades" :key="i">
                <v-list-item-content>
                  <v-list-item-title>
                    <v-chip
                      label
                      class="mr-2"
                      :color="grade.value >= 3 ? 'green' : 'red'"
                      text-color="white"
                    >
                      {{ grade.value }}
                    </v-chip>
                    {{ grade.descriptions }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </section>
</template>
<script>
export default {
  data: () => ({
    date: null,
    grades: [
      {
        name: 'Angielski',
        grades: [
          {
            value: 6,
            descriptions: 'Kartkówka',
            weight: 1,
          },
          {
            value: 4,
            descriptions: 'Odpowiedź',
            weight: 2,
          },
        ],
      },
      {
        name: 'Polski',
        grades: [
          {
            value: 6,
            descriptions: 'Kartkówka',
            weight: 1,
          },
          {
            value: 4,
            descriptions: 'Odpowiedź',
            weight: 2,
          },
          {
            value: 1,
            descriptions: 'Sprawzian',
            weight: 1,
          },
          {
            value: 4,
            descriptions: 'Odpowiedź',
            weight: 2,
          },
        ],
      },
    ],
  }),
}
</script>
