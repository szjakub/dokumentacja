export const schoolRegister = async function ({ commit }, params) {
  return await this.$axios.$post('/schools/', params)
}
export const login = async function ({ commit }, params) {
  const login = await this.$axios.$post('/api-token-auth/', params)
  return login
}
