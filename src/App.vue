<!-- @format -->

<template>
  <p class="logo">
    <img alt="logo" src="./assets/logo.png" />
  </p>
  <LTList />
  <div class="icons">
    <a
      href="https://github.com/xryuseix/lt"
      target="_blank"
      rel="noopener noreferrer"
      ><img src="./assets/github.png"/></a
    ><a
      href="https://xryuseix.github.io"
      target="_blank"
      rel="noopener noreferrer"
      ><img src="./assets/xryuseix.png"
    /></a>
  </div>
</template>

<script>
import LTList from "./components/LT_List.vue";

export default {
  name: "App",
  components: {
    LTList: LTList,
  },
};
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
.logo img {
  width: 40%;
  max-height: 500px;
  max-width: 500px;
}
.icons {
  margin: 30px;
}
.icons img {
  width: 50px;
  margin: 0 10px;
}
</style>
