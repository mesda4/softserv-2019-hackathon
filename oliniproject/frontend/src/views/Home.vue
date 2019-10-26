<template>
  <div class="home">
    <div class="navigation">
      <span class="right">
        <span class="button wide">
          <img class="icon" src="../assets/orphanage_logo.svg" />
          <span>Приют</span>
        </span>
      </span>
      <span class="left">
        <span class="button">
          <img class="icon" src="../assets/user.svg" />
          <span>Аккаунт</span>
        </span>
      </span>
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "home",
  components: {}
};
</script>

<style lang="scss" scoped>
.navigation {
  width: 100%;
  background-color: #333;
  display: flex;
  height: 5rem;
  align-items: center;
}
.icon {
  height: 2rem;
  filter: invert(1);
  margin: 0 5px;
}
.left {
  margin-left: auto;
}
.button {
  margin: 0 10px;
  display: flex;
  align-items: center;
  color: white;
  padding: 10px;
  border: 1px solid white;
  border-radius: 4px;
}
.wide {
  width: 12rem;
  justify-content: center;
}
.content {
  width: 100%;
  padding: 0 15%;
}
</style>