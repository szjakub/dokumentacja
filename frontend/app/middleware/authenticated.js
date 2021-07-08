export default function ({ store, redirect }) {
  // If the user is not authenticated
  if (store.state.user.token == null) {
    // return redirect('/login')
  } else {
    store.$axios.setToken(store.state.user.token, 'Token')
  }
}
