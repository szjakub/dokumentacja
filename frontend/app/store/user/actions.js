export const getIp = async ({ commit }) => {
  await this.$axios.$get('http://icanhazip.com')
  commit('SET_IP', 'haloo')
}

export const schoolRegister = async function ({ commit }, params) {
  const schoolPost = await this.$axios.$post('/schools/', params)
  return schoolPost
}
export const login = async function ({ commit }, params) {
  const login = await this.$axios.$post('/api-token-auth/', params)
  return login
}
