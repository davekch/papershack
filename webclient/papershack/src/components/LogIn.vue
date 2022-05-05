<template>
  <div>
    <h1>Log in</h1>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="username" />
      <br />
      <input v-model="password" placeholder="password" type="password" />
      <br />
      <button type="submit">Login</button>
    </form>
  </div>
</template>


<script>
import { mapMutations, mapGetters } from "vuex";

export default {
  data: () => {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapMutations(["setTokenAccess", "setTokenRefresh"]),
    ...mapGetters(["isAuthenticated"]),
    async login(e) {
      e.preventDefault();
      const response = await fetch("http://127.0.0.1:8000/api/token/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      });
      const { access, refresh } = await response.json();
      this.setTokenAccess(access);
      this.setTokenRefresh(refresh);
      if (this.isAuthenticated()) {
        this.$router.push("/records");
      }
    },
  },
};
</script>