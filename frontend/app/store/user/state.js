export default () => ({
  token:
    window.sessionStorage.getItem('token') != null
      ? window.sessionStorage.getItem('token')
      : null,
})
