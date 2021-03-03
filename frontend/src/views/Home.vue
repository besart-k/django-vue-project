<template>
  <div>
    <h2>Home Page</h2>
    <h3>
      <router-link to="/risk-types">Add risk based on risk type</router-link>
    </h3>
    <h3><router-link to="/risk-type-add">Define new risk type</router-link></h3>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>