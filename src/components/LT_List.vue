<!-- @format -->

<template>
  <h1>Welcome to my LT page</h1>
  <table>
    <tr>
      <th v-for="(column, key) in columns" :key="key">
        {{ column.label }}
      </th>
    </tr>
    <tr v-for="(row, key) in rows" :key="key" class="row">
      <td class="row title">
        {{ row.title }}
      </td>
      <td class="link">
        <a v-bind:href="row.link"> Link </a>
      </td>
      <td class="download">
        <a v-bind:href="row.download" download>[Download]</a>
      </td>
      <td class="update">
        {{ row.update }}
      </td>
    </tr>
  </table>
</template>

<script>
import slides from "../assets/slides.json";

export default {
  name: "LTList",
  components: {},
  data() {
    return {
      columns: [
        { label: "タイトル", field: "title" },
        { label: "Website Link", field: "link" },
        { label: "PDF Download", field: "download" },
        { label: "Update", field: "update" },
      ],
      rows: slides,
    };
  },
};
</script>

<style scoped>
a {
  color: #42b983;
  font-weight: bold;
}
table {
  margin-left: auto;
  margin-right: auto;
  border-collapse: collapse;
}
table .title {
  width: 40%;
}
table .link,
table .download,
table .update {
  width: 20%;
}
table .row {
  -webkit-transition: all 0.3s ease;
  -moz-transition: all 0.3s ease;
  -o-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
table .row:hover {
  background-color: #d6e9ca;
}
table tr {
  border-bottom: 1px dotted #8bc34a;
}
table td {
  padding: 1em 10px 1em 1em;
}
table th {
  border-bottom: 2px solid #18521b;
}
table tr:last-child {
  border-bottom: 2px solid #18521b;
}
</style>
