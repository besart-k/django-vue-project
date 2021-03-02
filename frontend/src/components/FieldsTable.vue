<template>
    <div>
        <b-table striped hover :items="getPropertiesTable()"></b-table>
    </div>
</template>

<script>
    export default {
        name:'FieldsTable',
        props:['properties', 'required'],
        methods: {
            getPropertiesTable() {
                console.log('called')
                var items = [];
                for (const [key, value] of Object.entries(this.properties)) {
                    var fieldIsRequired = this.required.includes(key);
                    items.push({
                        name: key,
                        type: value.type,
                        minimum: value.minimum||value.minLength||value.formatMinimum,
                        maximum: value.maximum||value.maxLength||value.formatMaximum,
                        integer: value.integer,
                        enumOptions: value.enumOptions,
                        required: fieldIsRequired,

                    }, );
                }
                return items;
            },

        }
    };
</script>