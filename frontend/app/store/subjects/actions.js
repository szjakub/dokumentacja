export const getSubjects = async function ({ commit }, params) {
  return await this.$axios.$get('/subjects/')
}
export const getSubject = async function ({ commit }, params) {
  return await this.$axios.$get(`/subjects/${params}/`)
}
export const updateSubject = async function ({ commit }, params) {
  return await this.$axios.$update(`/subjects/${params.id}/`, params)
}
export const deleteSubject = async function ({ commit }, params) {
  return await this.$axios.$delete(`/subjects/${params.id}/`)
}
