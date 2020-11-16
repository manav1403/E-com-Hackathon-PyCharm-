<template lang="pug">
  v-carousel(v-model='model' cycle='' height='100%' hide-delimiter-background='' show-arrows-on-hover='')
    v-carousel-item(v-for='(slide, i) in slides' :key='i')
      v-sheet(:color='colors[i]' height='100%')
        v-row.fill-height(align='center' justify='center')
          .display-3
            | {{ slide }} Slide

</template>

<script>
export default {
  name: 'HomeLanding',
  data () {
    return {
      model: 0,
      colors: [
        'primary',
        'secondary',
        'yellow darken-2',
        'red',
        'orange'
      ],
      slides: [
        'First',
        'Second',
        'Third',
        'Fourth',
        'Fifth'
      ]
    }
  }
}
</script>
