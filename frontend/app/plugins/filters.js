import Vue from 'vue'

Vue.filter('formatDateHour', (dateString) => {
  let time = dateString
  if (typeof dateString === 'string' || dateString instanceof Date) {
    time = new Date(dateString).getTime()
  }
  const date = new Date(parseInt(time))
  return date.toLocaleTimeString(navigator.language, {
    hour: '2-digit',
    minute: '2-digit',
  })
})
