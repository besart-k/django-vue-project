<template>
    <div>
        <h3>Generate Custom Forms</h3>
        <div class="add-field-container container">
            <b-tabs content-class="mt-3">
                <b-tab title="Add Text Field" active>
                    <div class="field-form-container">
                        <div class="field-attr">
                            <label>Field Name</label>
                            <input type="text" v-model="currentTextFormData.name" />
                        </div>
                        <div class="field-attr">
                            <label>Min length</label>
                            <input type="number" v-model="currentTextFormData.minLength" />
                        </div>
                        <div class="field-attr">
                            <label>Max Length</label>
                            <input type="number" v-model="currentTextFormData.maxLength" />
                        </div>
                        <div class="field-attr">
                            <label>Required</label>
                            <input type="checkbox" v-model="currentTextFormData.required" />
                        </div>
                        <div class="field-attr">
                            <button @click="addTextField">Add</button>
                        </div>
                    </div>
                </b-tab>
                <b-tab title="Add Number Field">
                    <div class="field-form-container">
                        <div class="field-attr">
                            <label>Field Name</label>
                            <input type="text" v-model="currentNumberFormData.name" />
                        </div>
                        <div class="field-attr">
                            <label>Minimum</label>
                            <input type="number" v-model="currentNumberFormData.minimum" />
                        </div>
                        <div class="field-attr">
                            <label>Maximum</label>
                            <input type="number" v-model="currentNumberFormData.maximum" />
                        </div>
                        <div class="field-attr">
                            <label>Required</label>
                            <input type="checkbox" v-model="currentNumberFormData.required" />
                        </div>
                        <div class="field-attr">
                            <button @click="addNumberField">Add</button>
                        </div>
                    </div>
                </b-tab>
                <b-tab title="Add Date Field">
                    <div class="field-form-container">
                        <div class="field-attr">
                            <label>Field Name</label>
                            <input type="text" v-model="currentDateFormData.name" />
                        </div>
                        <div class="field-attr">
                            <label>Minimum</label>
                            <input type="date" v-model="currentDateFormData.minimum" />
                        </div>
                        <div class="field-attr">
                            <label>Maximum</label>
                            <input type="date" v-model="currentDateFormData.maximum" />
                        </div>
                        <div class="field-attr">
                            <label>Required</label>
                            <input type="checkbox" v-model="currentDateFormData.required" />
                        </div>
                        <button @click="addDateField">Add</button>
                    </div>
                </b-tab>
                <b-tab title="Add Enum">
                    <div class="field-form-container">
                        <div class="field-attr">
                            <label>Field Name</label>
                            <input type="text" v-model="currentDateFormData.name" />
                        </div>

                        <div class="field-attr">
                            <label>Options</label>
                            <select>
                                <option v-for="[ind, item] in currentEnumFormData.enum.entries()" v-bind:key="ind">
                                    {{ item }}
                                </option>
                            </select>
                        </div>
                        <div class="field-attr">
                            <label>Add options to enum</label>
                            <p>
                                <input v-model="currentEnumFormData.input" />
                                <button @click="addEnumOption" id="add-option-button">
                                    Add option
                                </button>
                            </p>
                        </div>
                        <div class="field-attr">
                            <label>Required</label>
                            <input type="checkbox" v-model="currentDateFormData.required" />
                        </div>
                        <button @click="addDateField">Add</button>
                    </div>
                </b-tab>
            </b-tabs>
            <div>
                <b-table striped hover :items="getPropertiesTable()"></b-table>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "RiskDefinitionAdd",
        data: () => ({
            required: [],
            properties: {},
            currentTextFormData: {
                name: "",
                minLength: 0,
                maxLength: 100,
                required: true,
            },
            currentNumberFormData: {
                name: "",
                minimum: null,
                maximum: null,
                required: true,
            },
            currentDateFormData: {
                name: "",
                minimum: null,
                maximum: null,
                required: true,
            },
            currentEnumFormData: {
                name: "",
                enum: [],
                required: true,
                input: "",
            },
        }),
        methods: {
            addTextField() {
                const {
                    minLength,
                    maxLength,
                    name,
                    required
                } = this.currentTextFormData;
                this.properties[name] = {
                    type: "string",
                    title: name,
                    minLength: minLength,
                    maxLength: maxLength,
                };
                if (required) {
                    this.required.push(name);
                }
            },
            addNumberField() {
                const {
                    minimum,
                    maximum,
                    name,
                    required
                } = this.currentNumberFormData;
                this.properties[name] = {
                    type: "number",
                    minimum: minimum,
                    maximum: maximum,
                };
                if (required) {
                    this.required.push(name);
                }
            },
            addDateField() {
                const {
                    minimum,
                    maximum,
                    name,
                    required
                } = this.currentDateFormData;
                this.properties[name] = {
                    type: "string",
                    format: "date",
                    minimum: minimum,
                    maximum: maximum,
                };
                if (required) {
                    this.required.push(name);
                }
            },
            addEnumOption() {
                this.currentEnumFormData.enum.push(this.currentEnumFormData.input);
            },
            getPropertiesTable() {
                var items = [];
                for (const [key, value] of Object.entries(this.properties)) {
                    var field_is_required = this.required.includes(key);
                    const {
                        type,
                        title,
                        format,
                        minimum,
                        maximum,
                        minLength,
                        maxLength,
                    } = value;
                    items.push({
                        field_name: key,
                        type: type,
                        title: title,
                        format: format,
                        minimum: minimum,
                        maximum: maximum,
                        minLength: minLength,
                        maxLength: maxLength,
                        required: field_is_required,
                    });
                }
                return items;
            },
        },
    };
</script>
<style scoped>
    .add-field-container {
        width: 100%;
        align-self: center;
    }

    .field-form-container {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        flex-wrap: wrap;
        align-items: center;
    }

    button {
        cursor: pointer;
        height: 50px;
        border: none;
        background: #4caf50;
        color: #fff;
        margin: 0 0 5px;
        padding: 5px 10px;

        font-size: 15px;
    }

    .field-attr {
        display: flex;
        flex-direction: column;
    }

    #add-option-button {
        cursor: pointer;
        height: 30px;
        border: none;
        background: lightblue;
        color: #fff;
        margin: 0 0 5px;
        padding: 2px 5px;

        font-size: 15px;
    }
</style>