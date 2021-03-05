<template>
  <div class="form-container">
    <h3>Risk Type: {{ riskTypeName }}</h3>
    <FormSchema
      :schema="schema"
      v-model="model"
      ref="formSchema"
      @submit="submitRiskTypeData"
    >
      <button type="submit">Add {{ riskTypeName }}</button>
    </FormSchema>
  </div>
</template>

<script>
import FormSchema from "@formschema/native";
import RiskTypeServices from "../services/RiskTypeServices";
import { StatusCodes } from "http-status-codes";

export default {
  name: "RiskType",
  data: () => ({
    schema: {},
    model: {},
    riskTypeName: "",
  }),
  created() {
    var riskTypeId = this.$route.params.id;
    RiskTypeServices.getRiskType(riskTypeId)
      .then((response) => {
        const { name, definition } = response.data;
        this.$refs.formSchema.load(definition);
        this.riskTypeName = name;
      })
      .catch((error) => {
        console.log(error);
      });
  },

  methods: {
    submitRiskTypeData(ev) {
      ev.preventDefault();
      var riskTypeId = this.$route.params.id;

      RiskTypeServices.submitRiskTypeDate(riskTypeId, this.model)
        .then((response) => {
          if (response.status == StatusCodes.CREATED) {
            alert("The data was submited!");
            this.$refs.formSchema.reset();
          } else {
            alert("Something went wrong!");
          }
        })
        .catch((err) => {
          alert(err.message);
        });
    },
  },
  components: {
    FormSchema,
  },
};
</script>
<style>
.form-container {
  max-width: 700px;
  margin: auto;
  margin-bottom: 10px;
  background: #f9f9f9;
  padding: 25px;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}

label {
  margin-bottom: 0.5rem;
  font-size: 1rem;
  font-weight: 500;
  color: #212529;
  font-family: "Roboto", sans-serif;
}

.generated-input {
  border: none;
  box-shadow: 0 1px 2px 0 rgb(0 0 0 / 30%);
  background: #fff;
  width: 100%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #495057;
  align-self: center;
}

button[type="submit"] {
  cursor: pointer;
  width: 100%;
  border: none;
  background: #4caf50;
  color: #fff;
  margin: 0 0 5px;
  padding: 10px;
  font-size: 15px;
}

.form-container form {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  align-items: baseline;
}

div[data-fs-field] {
  width: 50%;
  min-width: 200px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  margin-bottom: 10px;
}

div[data-fs-field-input] {
  width: 100%;
}

input[type="checkbox"] {
  align-self: flex-start;
}
</style>