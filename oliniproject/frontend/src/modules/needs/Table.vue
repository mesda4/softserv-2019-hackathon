<template>
    <table>
        <thead>
          <tr>
              <th v-for="(value, index) in headers" :key="index">
                  {{value}}
              </th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(value, index) in data" :key="index">
              <td>{{value.type_name}}</td>
              <td>{{value.name}}</td>
              <td>{{value.quantity}}</td>
              <td>
                  <router-link v-if = "value.pet_name !== null" :to= "`/animals/${value.pet_id}`">
                        {{value.pet_name}}
                  </router-link>
                  <span v-if = "value.pet_name == null">
                      Для приюта
                  </span>
              </td>
          </tr>
        </tbody>
      </table>
</template>

<script>
export default {
    props: {
        headers: {
            type: Array,
            default: () => ['Тип','Название','Количество', 'Для кого']
        },
        data: {
            type: Array,
            default: () =>
            [
                {
                    type_name: 'Еда',
                    name: 'Chicken nuggets',
                    quantity: null,
                    pet_name: null,
                    pet_id: null
                }
            ]
        }
    }
}
</script>