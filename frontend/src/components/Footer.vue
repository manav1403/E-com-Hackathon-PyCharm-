<template lang="pug">
    v-footer(color='primary lighten-1' padless='')
      v-row(justify='center' no-gutters='')
        v-btn.my-2(v-for='link in links' :key='link' color='white' text='' rounded='')
          | {{ link }}
        v-col.primary.lighten-2.py-4.text-center.white--text(cols='12')
          | {{ new Date().getFullYear() }} &mdash;
          strong Vuetify

</template>
<script>
export default {
  name: 'Footer',
  data () {
    return {
      links: ['Home', 'Products', 'Cat1', 'Cat2', 'Cat3', 'Account']
    }
  }
}
</script>
