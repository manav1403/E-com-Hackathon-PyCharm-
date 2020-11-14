<template lang="pug">
  v-app
</template>

<script>
import { instance } from '@/api/axios'
export default {
  name: 'App',

  components: {
  },

  data: () => ({
  }),

  created () {
    instance.get('/auth/csrf-token/').then(response => {
      const token = response.data.csrftoken
      document.cookie = `csrftoken = ${token}`
    })
  }
}
</script>
