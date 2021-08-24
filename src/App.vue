<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <LT_List msg="Welcome to my LT index page"/>
</template>

<script>
import LT_List from './components/LT_List.vue'

export default {
  name: 'App',
  components: {
    LT_List
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
