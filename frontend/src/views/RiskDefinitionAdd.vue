<template>
  <div>
    <h3>Add risk type definition</h3>
    <div class="add-field-container container">
      <div class="risk-form-container">
        <input
          id="risk-type-name-id"
          v-model="riskTypeName"
          placeholder="Risk Type Ex: Price, Vehicle..."
        />
        <button @click="submitRiskType">Submit Definition</button>
      </div>
      <fields-table
        :properties="properties"
        :required="fieldsRequired"
      ></fields-table>

      <b-tabs content-class="mt-3">
        <b-tab title="Add Text Field" active>
          <add-text-field-form @addField="addField"></add-text-field-form>
        </b-tab>
        <b-tab title="Add Number Field">
          <add-number-field-form @addField="addField"></add-number-field-form>
        </b-tab>

        <b-tab title="Add Date Field">
          <add-date-field-form @addField="addField"></add-date-field-form>
        </b-tab>
        <b-tab title="Add Enum">
          <add-enum-field-form @addField="addField"></add-enum-field-form>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<script>
import FieldsTable from "../components/FieldsTable.vue";
import AddNumberFieldForm from "../components/AddNumberFieldForm.vue";
import AddTextFieldForm from "../components/AddTextFieldForm.vue";
import AddDateFieldFormVue from "../components/AddDateFieldForm.vue";
import AddEnumFieldFormVue from "../components/AddEnumFieldForm.vue";
import RiskTypeServices from "../services/RiskTypeServices";
import { StatusCodes } from "http-status-codes";

export default {
  name: "RiskDefinitionAdd",
  components: {
    "fields-table": FieldsTable,
    "add-number-field-form": AddNumberFieldForm,
    "add-text-field-form": AddTextFieldForm,
    "add-date-field-form": AddDateFieldFormVue,
    "add-enum-field-form": AddEnumFieldFormVue,
  },
  data: () => ({
    fieldsRequired: [],
    properties: {},
    riskTypeName: "",
  }),

  methods: {
    addField(obj) {
      const { key, property, required } = obj;
      if (this.properties.key) {
        alert(`Field with name ${key} already exist!`);
      }
      this.$set(this.properties, key, property);
      if (required && !this.fieldsRequired.includes(key)) {
        this.fieldsRequired.push(key);
      }
    },
    getSchema() {
      var schema = {
        type: "object",
      };
      schema.properties = this.properties;
      schema.fieldsRequired = this.fieldsRequired;
      return schema;
    },
    submitRiskType() {
      if (!this.riskTypeName) {
        alert("Add risk type name before submiting the definition!");
      }
      if (!this.properties) {
        alert("Add at least one risk type field before submiting!");
      }
      RiskTypeServices.submitRiskTypeDefinition(
        this.riskTypeName,
        this.getSchema()
      ).then((response) => {
        if (response.status == StatusCodes.CREATED) {
          alert("The data was submited!");
        } else {
          alert(response.statusText);
        }
      });
    },
  },
};
</script>

<style>
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

.risk-form-container {
  display: flex;
  width: 100%;
  justify-content: space-between;
  padding: 20px;
  align-content: flex-end;
}

#risk-type-name-id {
  width: 50%;
}
</style>