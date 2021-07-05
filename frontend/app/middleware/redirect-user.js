export default function ({ store, redirect }) {
  // console.log(store.$router.currentRoute.path)
  // console.log(store.$router.currentRoute.path.split('/'))
  // console.log(store.state.user.type)
  const data = store.$router.currentRoute.path.split('/')
  // console.log(store.$router.app.$router.currentRoute)
  // console.log(store.$router.currentRoute)
  switch (store.state.user.type) {
    case 'principal':
      if (!data.includes('principal')) {
        // console.log('redirect')
        // console.log(store.$router.app.$router.currentRoute)
        // console.log(store.$router.getRoutes())
        // redirect('/principal')
      }
      break
    //   case 'teacher':
    //     // redirect('/teacher')
    //     break
    //   case 'student':
    //     // redirect('/student')
    //     break
    default:
      console.log('jestem')
    //     store.commit('user/SET_TOKEN', null)
    //     // store.state.user.token = null
    // return redirect('/login')
  }
}
