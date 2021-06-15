export const actions = () => ({
  async getIP({ commit }) {
    await this.$axios.$get('http://icanhazip.com')
    commit('SET_IP', 'haloo')
  },
})
