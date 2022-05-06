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
export default {
  data: () => {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login(e) {
      e.preventDefault();
      this.$store
        .dispatch("auth/login", {
          username: this.username,
          password: this.password,
        })
        .then(
          () => {
            this.$router.push("/records");
          },
          (error) => {
            console.log(error);
          }
        );
    },
  },
};
</script>