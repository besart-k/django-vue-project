<template>
    <div>
        <h1>Risk Type Name : {{riskTypeName}}</h1>
            <FormSchema :schema="schema" v-model="model" ref="formSchema">
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
            schema: {},
            model: {},
            riskTypeName : '',
            endpoint: 'http://localhost:8000/risk-type-definitions/',
        }),
        created() {
            var riskTypeId = this.$route.params.id;
            this.setRiskType(riskTypeId);
        },

        methods: {
            setRiskType(id) {
                axios.get(`${this.endpoint}${id}`).then(response => {
                    const {name, definition} = response.data;
                    this.$refs.formSchema.load(definition)
                    this.riskTypeName = name;
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