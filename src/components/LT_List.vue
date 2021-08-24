<!-- @format -->

<template>
  <div class="lt_list">
    <h1>{{ msg }}</h1>
    <ul>
      <li>
        <a href="/lt/padlock/index.html"> padlock </a>
        <a href="/lt/padlock/download/slide.pdf" download>[download]</a>
      </li>
      <li>
        <a href="/lt/github-111days/index.html"> github-111days </a>
        <a href="/lt/github-111days/download/slide.pdf" download>[download]</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "LTList",
  props: {
    msg: String,
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
a {
  color: #42b983;
  font-weight: bold;
}
</style>
