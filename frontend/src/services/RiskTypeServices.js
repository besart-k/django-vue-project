import axios from "axios";


const client = axios.create({
    baseURL: process.env.VUE_APP_BASE_RISK_TYPE_API_URL
})


const RiskTypeServices = class {
    static getAllRiskTypes() {
        return client.get('/risk-type-definitions/')
    }

    static getRiskType(id) {
        return client.get(`http://localhost:8000/risk-type-definitions/${id}`)
    }

    static submitRiskTypeDate(id, data) {
        return client.post("http://localhost:8000/risk-type-data/", {
            risk_type_definition: id,
            data: data,
        })
    }

    static submitRiskTypeDefinition(name, definition) {
        return client.post("http://localhost:8000/risk-type-definitions/", {
            name: name,
            definition: definition,
        })

    }

}

export default RiskTypeServices