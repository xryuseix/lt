<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <LTList msg="Welcome to my LT index page"/>
</template>

<script>
import LTList from './components/LT_List.vue'

export default {
  name: 'App',
  components: {
    LTList
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
