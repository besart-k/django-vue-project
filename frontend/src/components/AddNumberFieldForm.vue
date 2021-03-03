<template>
    <div class="field-form-container">
        <div class="field-attr">
            <label>Field Name</label>
            <input type="text" v-model="name" />
        </div>
        <div class="field-attr">
            <label>Minimum</label>
            <input type="number" v-model="minimum" />
        </div>
        <div class="field-attr">
            <label>Maximum</label>
            <input type="number" v-model="maximum" />
        </div>
        <div class="field-attr">
            <label>Integer</label>
            <input type="checkbox" v-model="integer" />
        </div>
        <div class="field-attr">
            <label>Required</label>
            <input type="checkbox" v-model="required" />
        </div>
        <div class="field-attr">
            <button v-on:click="addField">Add</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'AddNumberFieldForm',
        props: [],
        data: () => ({
            name: "",
            minimum: "",
            maximum: "",
            integer: "",
            required: true,
        }),
        methods: {

            addField() {
                this.$emit('addField', {
                    key: this.name,
                    property: {
                        type: this.integer ? "integer" : "number",
                        title: this.name,
                        minimum: this.toIntOrUndefined(this.minimum),
                        maximum: this.toIntOrUndefined(this.maximum),
                        attrs: {
                            "min": this.toIntOrUndefined(this.minimum),
                            "max": this.toIntOrUndefined(this.maximum),
                            "step": this.integer ? undefined : "any"
                        }
                    },
                    required: this.required
                })

            },
            toIntOrUndefined(str) {
                if (!isNaN(parseInt(str))) {
                    return parseInt(str)
                }
                return undefined
            }
        }
    }
</script>