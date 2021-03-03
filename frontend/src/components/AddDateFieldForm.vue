<template>
    <div class="field-form-container">
        <div class="field-attr">
            <label>Field Name</label>
            <input type="text" v-model="name" />
        </div>
        <div class="field-attr">
            <label>Minimum</label>
            <input type="date" v-model="minimum" />
        </div>
        <div class="field-attr">
            <label>Maximum</label>
            <input type="date" v-model="maximum" />
        </div>
        <div class="field-attr">
            <label>Required</label>
            <input type="checkbox" v-model="required" />
        </div>
        <button @click="addField">Add</button>
    </div>
</template>

<script>
    export default {
        name: 'AddDateFieldForm',
        props: [],
        data: () => ({
            name: "",
            minimum: "",
            maximum: "",
            required: true,
        }),
        methods: {

            addField() {
                this.$emit('addField', {
                    key: this.name,
                    property: {
                        type: "string",
                        title: this.name,
                        format: "date",
                        formatMinimum: this.minimum,
                        formatMaximum: this.maximum,
                        attrs: {
                            type: "date",
                            min: this.minimum,
                            max: this.maximum
                        }
                    },
                    required: this.required
                })

            },
        }
    }
</script>