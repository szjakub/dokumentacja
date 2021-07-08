export const getTeachers = async function ({ commit }, params) {
  return await this.$axios.$get('/teachers/')
}
export const getTeacher = async function ({ commit }, params) {
  return await this.$axios.$get(`/teachers/${params}/`)
}
export const updateTeacher = async function ({ commit }, params) {
  return await this.$axios.$update(`/teachers/${params.id}/`, params)
}
export const deleteTeacher = async function ({ commit }, params) {
  return await this.$axios.$delete(`/teachers/${params.id}/`)
}
