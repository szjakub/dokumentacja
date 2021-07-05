export const getStudents = async function ({ commit }, params) {
  return await this.$axios.$get('/students/')
}
export const getStudent = async function ({ commit }, params) {
  return await this.$axios.$get(`/students/${params.id}`)
}
export const updateStudent = async function ({ commit }, params) {
  return await this.$axios.$update(`/students/${params.id}`, params)
}
export const deleteStudent = async function ({ commit }, params) {
  return await this.$axios.$delete(`/students/${params.id}`)
}
