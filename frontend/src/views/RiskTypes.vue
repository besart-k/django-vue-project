<template>
  <div>
    <h3>Choose a risk type to create new risk</h3>
    <div class="list-group list-group-flush container">
      <router-link class="list-group-item list-group-item-action bg-light" v-for="type in riskTypes"
        v-bind:key="type.id" :to="{ name: 'RiskType', params: { id: type.id } }">{{ type.name }}</router-link>
      <div v-if="noData">

        <h4>No risk types</h4>
        <router-link to="/risk-type-add">Create risk type definition</router-link>
      </div>
    </div>
  </div>
</template>

<script>
  import RiskTypeServices from "../services/RiskTypeServices"

  export default {
    name: "RiskTypes",
    data() {
      return {
        riskTypes: [],
        noData: false
      };
    },
    created() {
      RiskTypeServices.getAllRiskTypes().then((response) => {
          var data = response.data;
          if (data.length !== 0) {
            this.riskTypes = data
          } else {
            this.noData = true
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  };
</script>

<style scoped>
  .list-group-flush {
    width: 50%;
    align-self: center;
  }
</style>