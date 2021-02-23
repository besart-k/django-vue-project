<template>
  <div id="app">
    <header>
      <h1>List of Risk Types</h1>
    </header>
    <main>
      <aside class="sidebar">
        <div v-for="type in riskTypes" v-bind:key="type.id">
          {{ type.name }}
        </div>
      </aside>
      <div class="content">
      </div>
    </main>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'App',
    data() {
      return {
        riskTypes: [],
        endpoint: 'http://localhost:8000/risk-type-definitions/'
      }
    },
    created() {
      this.getAllRiskTypes();
    },

    methods: {
      getAllRiskTypes() {
        axios.get(this.endpoint).then(response => {
          this.riskTypes = response.data;
        }).catch(error => {
          console.log('-----error-------');
          console.log(error);
        })
      }
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