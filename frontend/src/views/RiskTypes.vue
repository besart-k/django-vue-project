<template>
    <div>
        <h1>The list of Risk Types</h1>
        <div class="list-group list-group-flush container">
            <router-link class="list-group-item list-group-item-action bg-light" v-for="type in riskTypes" v-bind:key="type.id"
                :to="{ name: 'RiskType', params: { id: type.id } }">{{type.name}}</router-link>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "RiskTypes",
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
                    console.log(error);
                })
            }
        }
    }
</script>

<style scoped>
.list-group-flush{
    width:30%;
    align-self:center;
}
</style>