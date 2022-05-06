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
import UserService from "../services/user.service";

export default {
  name: "RecordsList",
  data() {
    return {
      records: [],
    };
  },
  mounted() {
    UserService.getRecords().then(
      (response) => {
        this.records = response.data.results;
      },
      (error) => {
        console.log(error);
      }
    );
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
