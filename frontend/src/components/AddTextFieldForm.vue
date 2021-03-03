<template>
  <div class="field-form-container">
    <div class="field-attr">
      <label>Field Name</label>
      <input type="text" v-model="name" />
    </div>
    <div class="field-attr">
      <label>Min length</label>
      <input type="number" min="0" v-model="minLength" />
    </div>
    <div class="field-attr">
      <label>Max Length</label>
      <input type="number" v-model="maxLength" />
    </div>
    <div class="field-attr">
      <label>Required</label>
      <input type="checkbox" v-model="required" />
    </div>
    <div class="field-attr">
      <button @click="addField">Add</button>
    </div>
  </div>
</template>

<script>
import { toIntOrUndefined } from "../services/utils";
export default {
  name: "AddTextFieldForm",
  props: [],
  data: () => ({
    name: "",
    minLength: "",
    maxLength: "",
    required: true,
  }),
  methods: {
    addField() {
      if (this.minLength && this.maxLength && this.minLength > this.maxLength) {
        alert("Minimum cannot be greater than maximum!");
        return;
      }
      if (!this.name) {
        alert("Name field cannot be empty!");
        return;
      }
      this.$emit("addField", {
        key: this.name,
        property: {
          type: "string",
          title: this.name,
          minLength: toIntOrUndefined(this.minLength),
          maxLength: toIntOrUndefined(this.maxLength),
          attrs: {
            class: "generated-input gt-input",
            placeholder: this.name,
          },
        },
        required: this.required,
      });
    },
  },
};
</script>