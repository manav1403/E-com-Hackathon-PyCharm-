<template lang="pug">
v-card.elevation-2
  v-app-bar(app, clipped-right, flat, floating, style="opacity:1.0")
    v-app-bar-nav-icon.hidden-md-and-up(@click.stop="drawer = !drawer")
    v-toolbar-title.hidden-sm-and-down.white--text
      span.title.ml-3.mr-5(text, style="color:black") Shopping Site&nbsp;
    v-spacer
    .hidden-sm-and-down
      v-btn.pa-2.ma-1(
        text,
        v-for="link in links",
        :key="link.text",
        label,
        exact
      ) {{ link.text }}
    v-btn(icon='')
      v-icon mdi-cart
  v-navigation-drawer(
    v-model="drawer",
    app,
    left,
    temporary,
    style="z-index:5"
  )
    v-list(dense)
      v-list-item(v-for="link in links", :key="link.text", @click="", exact)
        v-list-item-action
          v-icon {{ link.icon }}
        v-list-item-content
          v-list-item-title.grey--text {{ link.text }}
</template>

<script>
export default {
  name: 'Header',

  data () {
    return {
      drawer: null,
      links: [
        { text: 'Home', icon: 'mdi-home' },
        { text: 'All Products', icon: 'mdi-shopping' },
        { text: 'Cat1', icon: 'mdi-laptop' },
        { text: 'Cat2', icon: 'mdi-cellphone' },
        { text: 'Cat3', icon: 'mdi-robot' },
        { text: 'Account', icon: 'mdi-account' }
      ]
    }
  }
}
</script>

<style scoped></style>
