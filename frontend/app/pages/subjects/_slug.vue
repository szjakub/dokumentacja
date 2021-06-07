<template>
  <div>SLUG PAGE {{ $route.params }}</div>
</template>
<script>
export default {
  mounted() {
    console.log(this.$route)
  },
}
</script>
