<template>
    <div v-if="pet" class="pet block">
        <!-- MAIN IMG -->
        <div class="main-img">
            <img src="../1/1.1.jpg" />
        </div>

        <div class="inner-wrap">
            <!-- IMGS -->
            <div class="toggle-gallery-btn">
                <button class="waves-effect waves-light btn">
                    SHOW MORE PHOTOS
                    <i class="material-icons right">image</i>
                </button>    
            </div>

            <div class="gallery">
                <div><img src="../1/1.2.jpg" alt=""></div>
                <div><img src="../1/1.3.jpg" alt=""></div>
                <div><img src="../1/1.4.jpg" alt=""></div>
                <div><img src="../1/1.5.jpg" alt=""></div>
            </div>

            <div class="info">
                <span>Name: </span>
                <span>{{pet.name}}</span>
            </div>
            <div class="info">
                <span>Breed: </span>
                <span>{{pet.breed}}</span>
            </div>
            <div class="info">
                <span>Description: </span>
                <span>{{pet.desc}}</span>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
    .pet {
        margin: 0 auto;
        width: 500px;
    }

    .main-img {
        width: 500px;

        img {
            width: 100%;
        }
    }

    .inner-wrap {
        width: 420px;
        margin: 0 auto;
    }

    .toggle-gallery-btn {
        text-align: center;
        margin: 1rem 0;
    }

    .gallery {
        display: flex;
        flex-wrap: wrap;

        margin: 0 auto;
        
        & > div {
            display: flex;
            justify-content: center;
            align-items: center;

            background: #eee;
            border-radius: 10px;
            width: 120px;
            margin: 10px;
            padding: 15px;

            cursor: pointer;
            transition: padding .3s;
            
            img {
                width: 100%;
            }

            &:hover {
                padding: 10px;
            }
        }
    }
</style>

<script>
export default {
    data: () => ({
        
    }),
    computed: {
        pet() {
            return this.$store.state.pets.pet;
        }
    },
    created() {
        const petId = this.$route.params.id;

        this.$store.dispatch("getPet", petId);
    }
}
</script>