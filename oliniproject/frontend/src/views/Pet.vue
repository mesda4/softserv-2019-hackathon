<template>
    <div v-if="pet">
        <img :src="pet.img" />
        <div>{{pet.name}}</div>
        <div>{{pet.breed}}</div>
        <div>{{pet.desc}}</div>
    </div>
</template>

<script>
export default {
    data: () => ({
        
    }),
    computed: {
        pet() {
            return this.$store.state.pets.pet
        }
    },
    created() {
        const petId = this.$route.params.id;

        this.$store.dispatch("getPet", petId);
    }
}
</script>