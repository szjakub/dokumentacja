export default function ({ $axios, store, redirect }) {
  $axios.onError((error) => {
    if (
      error.response &&
      (error.response.status === 500 || error.response.status === 401)
    ) {
      redirect('/login')
      store.commit('user/SET_TOKEN', '')
      store.commit('user/SET_TYPE_USER', '')
    }
  })
}
