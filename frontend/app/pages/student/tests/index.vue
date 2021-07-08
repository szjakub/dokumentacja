<template>
  <v-row justify="center">
    <v-col md="4" lg="3">
      <v-date-picker
        v-model="date"
        class="mt-4"
        @change="getTests"
      ></v-date-picker>
    </v-col>
    <v-col md="8" lg="9">
      <v-list two-line>
        <v-list-item-group>
          <template v-for="(item, index) in items">
            <v-list-item :key="item.title" @click="checkTest(item)">
              <template>
                <v-list-item-content>
                  <v-list-item-title v-text="item.title"></v-list-item-title>

                  <v-list-item-subtitle
                    class="text--primary"
                    v-text="item.headline"
                  ></v-list-item-subtitle>

                  <v-list-item-subtitle
                    v-text="item.subtitle"
                  ></v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-action>
                  <v-list-item-action-text
                    v-text="item.action"
                  ></v-list-item-action-text>
                </v-list-item-action>
              </template>
            </v-list-item>

            <v-divider v-if="index < items.length - 1" :key="index"></v-divider>
          </template>
        </v-list-item-group>
      </v-list>
      <v-bottom-sheet v-model="sheet">
        <v-sheet class="text-center" height="200px">
          <v-btn class="mt-6" text color="red" @click="sheet = !sheet">
            close
          </v-btn>
          <div class="py-3">
            {{ selected }}
          </div>
        </v-sheet>
      </v-bottom-sheet>
    </v-col>
  </v-row>
</template>
<script>
export default {
  data: () => ({
    sheet: false,
    selected: null,
    date: new Date().toISOString().substr(0, 10),
    items: [
      {
        action: '12-20-2020',
        headline: 'Brunch this weekend?',
        subtitle: `I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
        title: 'Ali Connors',
        extraContent: true,
        descriptions: `I'll be in your neighborhood doing errands this weekend. Do you want to hang out I'll be in your neighborhood doing errands this weekend. Do you want to hang out`,
      },
      {
        action: '12-20-2020',
        headline: 'Summer BBQ',
        subtitle: `Wish I could come, but I'm out of town this weekend.`,
        title: 'me, Scrott, Jennifer',
      },
      {
        action: '12-20-2020',
        headline: 'Oui oui',
        subtitle: 'Do you have Paris recommendations? Have you ever been?',
        title: 'Sandra Adams',
      },
      {
        action: '12-20-2020',
        headline: 'Birthday gift',
        subtitle:
          'Have any ideas about what we should get Heidi for her birthday?',
        title: 'Trevor Hansen',
      },
      {
        action: '12-20-2020',
        headline: 'Recipe to try',
        subtitle:
          'We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
        title: 'Britta Holt',
      },
    ],
  }),
  created() {},
  mounted() {},
  methods: {
    checkTest(tests) {
      if (
        Object.prototype.hasOwnProperty.call(tests, 'extraContent') &&
        tests.extraContent
      ) {
        this.selected = tests
        this.sheet = !this.sheet
      }
    },
    getTests() {
      // get homewroks
      console.log(this.date)
    },
  },
}
</script>
