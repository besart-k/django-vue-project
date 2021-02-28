<template>
  <div class="form-container">
    <h3>Risk Type Name : {{ riskTypeName }}</h3>
    <FormSchema :schema="schema" v-model="model" ref="formSchema" @submit="submitRiskTypeData">
      <button type="submit">Subscribe</button>
    </FormSchema>
  </div>
</template>

<script>
  import FormSchema from "@formschema/native";
  import axios from "axios";
  import {
    StatusCodes
  } from "http-status-codes";

  export default {
    name: "RiskType",
    data: () => ({
      schema: {},
      model: {},
      riskTypeName: "",
    }),
    created() {
      var riskTypeId = this.$route.params.id;
      this.setRiskType(riskTypeId);
    },

    methods: {
      setRiskType(id) {
        axios
          .get(`http://localhost:8000/risk-type-definitions/${id}`)
          .then((response) => {
            const {
              name,
              definition
            } = response.data;
            this.$refs.formSchema.load(definition);
            this.riskTypeName = name;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      submitRiskTypeData(ev) {
        ev.preventDefault();
        var riskTypeId = this.$route.params.id;
        axios
          .post("http://localhost:8000/risk-type-data/", {
            risk_type_definition: riskTypeId,
            data: this.model,
          })
          .then((response) => {
            if (response.status == StatusCodes.CREATED) {
              alert("The data was submited!");
              this.$refs.formSchema.reset();
            } else {
              alert("Something went wrong!");
            }
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

  input[type="text"],
  input[type="email"],
  input[type="datetime-local"],
  input[type="datetime"],
  input[type="password"],
  input[type="url"],
  select,
  textarea {
    border: none;
    box-shadow: 0 1px 2px 0 rgb(0 0 0 / 10%);
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
    width: 300px;
    padding: 10px;

    align-items: left;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 10px;
  }

  div[data-fs-field-input] {
    width: 100%;
    justify-content: flex-start;
    display: flex;
    flex-direction: column;
  }

  input[type="checkbox"] {
    align-self: flex-start;
  }
</style>