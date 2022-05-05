<template>
  <div class="records_container">
    <div class="records_content">
      <h1>Records</h1>
      <ul class="records_list">
        <li v-for="record in records" :key="record.id">
          <ul>
            {{
              record.title
            }}
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "RecordsList",
  data() {
    return {
      records: [],
    };
  },
  methods: {
    ...mapGetters(["getTokenAccess"]),
    async getData() {
      const token = this.getTokenAccess();
      try {
        const response = await fetch("http://127.0.0.1:8000/api/records/", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: "Bearer " + token,
          },
        });
        const result = await response.json();
        this.records = result.results;
        console.log("the thing:");
        console.log(result);
        console.log("the results:");
        console.log(result.results);
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getData();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
a {
  color: #42b983;
}
</style>
