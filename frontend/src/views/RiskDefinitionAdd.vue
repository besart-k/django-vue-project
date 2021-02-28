<template>
    <div>
        <h3>Generate Custom Forms</h3>
        <div class="add-field-container container">
            <b-tabs content-class="mt-3">
                <b-tab title="Add Text Field" active>
                    <div class="field-form-container">
                        <div class="field-attr">
                            <label>Field Name</label>
                            <input type="text" v-model="generalFormData.name" />
                        </div>
                        <div class="field-attr">
                            <label>Min length</label>
                            <input type="number" v-model="generalFormData.minLength" />
                        </div>
                        <div class="field-attr">
                            <label>Max Length</label>
                            <input type="number" v-model="generalFormData.maxLength" />
                        </div>
                        <div class="field-attr">
                            <label>Required</label>
                            <input type="checkbox" v-model="generalFormData.required" />
                        </div>
                        <div class="field-attr">
                            <button @click="addField('text')">Add</button>
                        </div>
                    </div>
                </b-tab>
                <b-tab title="Add Number Field">
                    <div class="field-form-container">
                        <div class="field-attr">
                            <label>Field Name</label>
                            <input type="text" v-model="generalFormData.name" />
                        </div>
                        <div class="field-attr">
                            <label>Minimum</label>
                            <input type="number" v-model="generalFormData.minimum" />
                        </div>
                        <div class="field-attr">
                            <label>Maximum</label>
                            <input type="number" v-model="generalFormData.maximum" />
                        </div>
                        <div class="field-attr">
                            <label>Required</label>
                            <input type="checkbox" v-model="generalFormData.required" />
                        </div>
                        <div class="field-attr">
                            <button @click="addField('number')">Add</button>
                        </div>
                    </div>
                </b-tab>
                <b-tab title="Add Date Field">
                    <div class="field-form-container">
                        <div class="field-attr">
                            <label>Field Name</label>
                            <input type="text" v-model="generalFormData.name" />
                        </div>
                        <div class="field-attr">
                            <label>Minimum</label>
                            <input type="date" v-model="generalFormData.minimum" />
                        </div>
                        <div class="field-attr">
                            <label>Maximum</label>
                            <input type="date" v-model="generalFormData.maximum" />
                        </div>
                        <div class="field-attr">
                            <label>Required</label>
                            <input type="checkbox" v-model="generalFormData.required" />
                        </div>
                        <button @click="addField('date')">Add</button>
                    </div>
                </b-tab>
                <b-tab title="Add Enum">
                    <div class="field-form-container">
                        <div class="field-attr">
                            <label>Field Name</label>
                            <input type="text" v-model="generalFormData.name" />
                        </div>

                        <div class="field-attr">
                            <label>Options</label>
                            <select>
                                <option v-for="[ind, item] in generalFormData.enum.entries()" v-bind:key="ind">
                                    {{ item }}
                                </option>
                            </select>
                        </div>
                        <div class="field-attr">
                            <label>Add options to enum</label>
                            <p>
                                <input v-model="generalFormData.enumInputOptionValue" />
                                <button @click="addEnumOption" id="add-option-button">
                                    Add option
                                </button>
                            </p>
                        </div>
                        <div class="field-attr">
                            <label>Required</label>
                            <input type="checkbox" v-model="generalFormData.required" />
                        </div>
                        <button @click="addField('enum')">Add</button>
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
            generalFormData: {
                name: "",
                minLength: null,
                maxLength: null,
                minimum: null,
                maximum: null,
                enum: [],
                enumInputOptionValue: '',
                required: true,
            },
        }),
        methods: {
            addField(type) {
                const {
                    name,
                    minLength,
                    maxLength,
                    minimum,
                    maximum,
                    required
                } = this.generalFormData
                if (!name) {
                    alert('Name cannot be empty!')
                    return
                }
                if (this.properties[name]) {
                    alert(`Field with name ${name} already exist!`)
                    return
                }

                if (type == 'text') {
                    this.properties[name] = {
                        type: "string",
                        title: name,
                        minLength: minLength,
                        maxLength: maxLength
                    }
                }
                if (type == 'number') {
                    this.properties[name] = {
                        type: "number",
                        minimum: minimum,
                        maximum: maximum,
                    }

                }
                if (type == 'date') {
                    this.properties[name] = {
                        type: "string",
                        title: "name",
                        format: "date",
                        minimum: minimum,
                        maximum: maximum,
                        "attrs": {
                            "type": "date"
                        }
                    }

                }
                if (type == 'enum') {
                    this.properties[name] = {
                        type: "string",
                        title: "name",
                        enum: this.generalFormData.enum,
                    }
                }
                if (required && !this.required.includes(name)) {
                    this.required.push(name);
                }
                this.resetGeneralForm()

            },
            resetGeneralForm() {
                this.generalFormData = Object.assign({}, {
                    name: "",
                    minLength: 0,
                    maxLength: 100,
                    minimum: 0,
                    maximum: 1000,
                    enum: [],
                    enumInputOptionValue: '',
                    required: true,

                })
            },
            addEnumOption() {
                const {
                    enumInputOptionValue
                } = this.generalFormData
                if (this.generalFormData.enum.includes(enumInputOptionValue)) {
                    alert('This option already exist!')
                    return
                }
                this.generalFormData.enum.push(enumInputOptionValue);
            },
            getPropertiesTable() {
                var items = [];
                for (const [key, value] of Object.entries(this.properties)) {
                    var field_is_required = this.required.includes(key);
                    items.push({
                        name: key,
                        minLength: value.minLength,
                        maxLength: value.maxLength,
                        minimum: value.minimum,
                        maximum: value.maximum,
                        enum: value.enum,
                        required: field_is_required,

                    }, );
                }
                return items;
            },
        }
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