<template>
  <table>
    <thead>
      <tr>
        <th v-for="(value, index) in headers" :key="index">{{value}}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(value, index) in data" :key="index">
        <td>{{value.type_name}}</td>
        <td>{{value.name}}</td>
        <td>
          <router-link
            v-if="value.pet_name !== null"
            :to="`/pets/${value.pet_id}`"
          >{{value.pet_name}}</router-link>
          <span v-if="value.pet_name == null">Для приюта</span>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import NeedService from "../../services/needs-service";

export default {
  props: {
    headers: {
      type: Array,
      default: () => ["Тип", "Название", "Для кого"]
    },
    data: {
      type: Array,
      default: () => [
        {
          type_name: "Еда",
          name: "Chicken nuggets",
          pet_name: null,
          pet_id: null
        },
        {
          type_name: "Еда",
          name: "Hamburger",
          pet_name: "Валера",
          pet_id: 0
        }
      ]
    }
  },
  async beforeMount() {
    this.$props.data = await NeedService.getNeeds();
  }
};
</script>