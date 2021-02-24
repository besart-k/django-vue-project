<template>
    <div>
        <h1>This is a Risk Type {{$route.params.id}}</h1>
        <FormSchema :schema="schema" v-model="model">
            <button type="submit">Subscribe</button>
        </FormSchema>
    </div>
</template>

<script>
    import FormSchema from '@formschema/native'
    import axios from 'axios'

    export default {
        name: "RiskType",
        data: () => ({
            schema: {"type":"object","properties":{"name":{"type":"string","ui":{"label":"Name","description":"Please fill in your name","placeholder":"Name"},"rules":{"required":true,"minLength":10}},"email":{"type":"string","ui":{"label":"Email"},"rules":{"required":true,"email":{"value":true,"errMsg":"Please fill in a valid email address"}}},"age":{"type":"integer","ui":{"label":"Age"}},"adult":{"type":"boolean","ui":{"label":"Adult","help":{"show":true,"text":"?","content":"Adults can play games"}}}}},
            model: {},
            endpoint: 'http://localhost:8000/risk-type-definitions/'
        }),
        created() {
            // console.log(this.$route.params.id)
            this.getRiskType(this.$route.params.id);
        },

        methods: {
            getRiskType(id) {
                axios.get(`${this.endpoint}${id}`).then(response => {
                    this.schema = response.data.definition;
                }).catch(error => {
                    console.log(error);
                })
            }
        },
        components: {
            FormSchema
        }
    }
</script>