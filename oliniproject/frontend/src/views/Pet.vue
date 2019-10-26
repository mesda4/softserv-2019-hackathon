<template>
  <div v-if="pet" class="pet block">
    <!-- MAIN IMG -->
    <div class="main-img">
      <img src="../1/1.1.jpg" />

      <div>
        <button @click="addPet(pet.id)" class="add-pet-btn round-btn waves-effect waves-light btn">
          <i class="material-icons">add</i>
        </button>
      </div>
    </div>

    <div class="inner-wrap">
      <div class="title">
        <h5>GALLERY</h5>
      </div>

      <div class="toggle-gallery-btn">
        <button @click="isGalleryShowed = !isGalleryShowed" class="waves-effect waves-light btn">
          {{isGalleryShowed ? "HIDE PHOTOS" : "SHOW MORE PHOTOS"}}
          <i
            class="material-icons right"
          >image</i>
        </button>
      </div>

      <div class="gallery" v-if="isGalleryShowed">
        <div>
          <img src="../1/1.2.jpg" alt />
        </div>
        <div>
          <img src="../1/1.3.jpg" alt />
        </div>
        <div>
          <img src="../1/1.4.jpg" alt />
        </div>
        <div>
          <img src="../1/1.5.jpg" alt />
        </div>
      </div>

      <!-- INFO -->
      <div class="title">
        <h5>INFO</h5>
      </div>
      <div class="info">
        <div>Name</div>
        <div>{{pet.name}}</div>
      </div>
      <div class="info">
        <div>Breed</div>
        <div>{{pet.breed}}</div>
      </div>
      <div class="info">
        <div>Description</div>
        <div>{{pet.desc}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    isGalleryShowed: false
  }),
  computed: {
    pet() {
      return this.$store.state.pets.pet;
    }
  },
  methods: {
    addPet(petId) {
      this.$store.dispatch("addPet");
    }
  },
  created() {
    const petId = this.$route.params.id;

    this.$store.dispatch("getPet", petId);
  }
};
</script>


<style lang="scss" scoped>
.pet {
  margin: 0 auto;
  width: 450px;
}

.main-img {
  position: relative;
  width: 100%;

  img {
    width: 100%;
  }
}

.add-pet-btn {
  position: absolute;
  right: 1.5rem;
  bottom: 1.5rem;
}

.inner-wrap {
  width: 420px;
  margin: 0 auto;
}

.title {
  text-align: center;
  margin-bottom: 10px;
}

.toggle-gallery-btn {
  text-align: center;
  margin: 1rem 0;
}

.gallery {
  display: flex;
  flex-wrap: wrap;

  margin: 0 auto;
  animation: block-appear 0.3s 1;

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
    transition: padding 0.3s;

    img {
      width: 100%;
    }

    &:hover {
      padding: 10px;
    }
  }
}

@keyframes block-appear {
  from {
    transform: scaleY(0);
  }
  to {
    transform: scaleY(1);
  }
}

.info {
  margin: 10px 0;

  & > div:first-child {
    font-weight: bold;
  }
}
</style>