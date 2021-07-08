export const SET_TOKEN = (state, data) => {
  state.token = data
  window.sessionStorage.setItem('token', data)
}
export const SET_TYPE_USER = (state, data) => {
  state.type = data
  window.sessionStorage.setItem('type', data)
}
