export default () => ({
  token:
    window.sessionStorage.getItem('token') != null
      ? window.sessionStorage.getItem('token')
      : null,
  type:
    window.sessionStorage.getItem('type') != null
      ? window.sessionStorage.getItem('type')
      : null,
})
