<template>
  <div class="field-form-container">
    <div class="field-attr">
      <label>Field Name</label>
      <input type="text" v-model="name" />
    </div>
    <div class="field-attr">
      <label>Min length</label>
      <input type="number" v-model="minLength" />
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
      this.$emit("addField", {
        key: this.name,
        property: {
          type: "string",
          title: this.name,
          minimum: this.toIntOrUndefined(this.minLength),
          maximum: this.toIntOrUndefined(this.maxLength),
        },
        required: this.required,
      });
    },
    toIntOrUndefined(str) {
      if (!isNaN(parseInt(str))) {
        return parseInt(str);
      }
      return undefined;
    },
  },
};
</script>