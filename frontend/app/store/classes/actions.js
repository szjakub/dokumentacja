export const getClasses = async function ({ commit }, params) {
  return await this.$axios.$get('/classes/')
}
export const getClass = async function ({ commit }, params) {
  return await this.$axios.$get(`/classes/${params}/`)
}
export const updateClass = async function ({ commit }, params) {
  return await this.$axios.$update(`/classes/${params.id}/`, params)
}
export const deleteClass = async function ({ commit }, params) {
  return await this.$axios.$delete(`/classes/${params.id}/`)
}
