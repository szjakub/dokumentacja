<template>
  <div class="pa-1 text-truncate">
    <span class="caption font-weight-bold">{{ event.name }}</span>
  </div>
</template>
<script>
export default {
  props: {
    event: {
      required: true,
      type: Object,
    },
  },
}
</script>
