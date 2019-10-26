<template>
    <div class="pets">
        <div v-if="pets.length === 0">NO PETS</div>
        <router-link
            tag="div"
            :to="'pets/' + pet.id"
            class="pet block" 
            v-for="pet in pets" :key="pet.id"
        >
            <img src="../../1/1.1.jpg" alt="">
            <div class="status">{{pet.status}}</div>  
        </router-link>
    </div>
</template>

<script>
export default {
    data: () => ({
    }),
    computed: {
        pets() {
            return this.$store.state.pets.pets;
        }
    },
    created() {
        this.$store.dispatch("getPets");
    }
}
</script>

<style lang="scss" scoped>
.pets {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.pet {
    width: 450px;

    cursor: pointer;

    &:not(:last-child) {
        margin-bottom: 3rem;
    }

    img {
        display: block;
        width: 100%;
    }
}

.status {
    text-align: center;
    padding: 10px 0;
}
</style>