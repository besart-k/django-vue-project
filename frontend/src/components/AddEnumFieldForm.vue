<template>
  <div class="field-form-container">
    <div class="field-attr">
      <label>Field Name</label>
      <input type="text" v-model="name" />
    </div>

    <div class="field-attr">
      <label>Options</label>
      <select>
        <option v-for="[ind, item] in enumOptions.entries()" v-bind:key="ind">
          {{ item }}
        </option>
      </select>
    </div>
    <div class="field-attr">
      <label>Add option</label>
      <p>
        <input v-model="enumOptionsInputOptionValue" />
        <button @click="addenumOptionsOption" id="add-option-button">
          Add option
        </button>
      </p>
    </div>
    <div class="field-attr">
      <label>Required</label>
      <input type="checkbox" v-model="required" />
    </div>
    <button @click="addField('enumOptions')">Add</button>
  </div>
</template>

<script>
export default {
  name: "AddenumOptionsFieldForm",
  props: [],
  data: () => ({
    name: "",
    enumOptions: [],
    enumOptionsInputOptionValue: "",
    required: true,
  }),
  methods: {
    addField() {
      this.$emit("addField", {
        key: this.name,
        property: {
          type: "string",
          title: this.name,
          enum: this.enumOptions,
          attrs: {
            placeholder: this.name,
            class: "generated-input ge-input",
          },
        },
        required: this.required,
      });
    },
    addenumOptionsOption() {
      if (this.enumOptions.includes(this.enumOptionsInputOptionValue)) {
        alert("This option already exist!");
        return;
      }
      this.enumOptions.push(this.enumOptionsInputOptionValue);
    },
  },
};
</script>
