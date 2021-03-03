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
import { toIntOrUndefined } from "../services/utils";
export default {
  name: "AddNumberFieldForm",
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
      if (!this.name) {
        alert("Name cannot be empty!");
        return;
      }
      if (!isNaN(this.minimum) && !isNaN(this.maximum) && this.minimum > this.maximum) {
        alert("Minimum cannot be greater than maximum.");
        return;
      }
      this.$emit("addField", {
        key: this.name,
        property: {
          type: this.integer ? "integer" : "number",
          title: this.name,
          minimum: toIntOrUndefined(this.minimum),
          maximum: toIntOrUndefined(this.maximum),
          attrs: {
            min: toIntOrUndefined(this.minimum),
            max: toIntOrUndefined(this.maximum),
            step: this.integer ? undefined : "any",
            class: "generated-input gn-input",
          },
        },
        required: this.required,
      });
    },
  },
};
</script>