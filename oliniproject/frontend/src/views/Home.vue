<template>
  <div class="home">
    <div class="navigation">
      <span class="right">
        <span class="button wide">
          <img class="icon" src="../assets/orphanage_logo.svg" />
          <span>Приют</span>
          <DropDown>
            <template slot="btn"></template>
            <template slot="body">
              <ul>
                <li class="dropitem">
                  <router-link to="/">Животные</router-link>
                </li>
                <li class="dropitem">
                  <router-link to="/needs">Нужды</router-link>
                </li>
                <li class="dropitem">
                  <router-link to="/contacts">Контакты</router-link>
                </li>
              </ul>
            </template>
          </DropDown>
        </span>
      </span>
      <span class="left">
        <router-link
          class="button"
          to="/account"
          tag="span"
        >
          <img class="icon" src="../assets/user.svg" />
          <span>Аккаунт</span>
        </router-link>
      </span>
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import DropDown from "bp-vuejs-dropdown";

export default {
  name: "home",
  components: { 
    DropDown 
  }
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
  cursor: pointer;
  margin: 0 10px;
  display: flex;
  align-items: center;
  color: white;
  padding: 10px;
  border: 1px solid white;
  border-radius: 4px;
}
.button:hover {
  background-color: #404040;
}
.wide {
  width: 12rem;
  justify-content: center;
}
.content {
// <<<<<<< HEAD
  max-width: 992px;
  margin: 0 auto;
  padding: 3rem;
// =======
//   padding: 6rem;
//   width: 100%;
// >>>>>>> d0d4fb6faf1b890ef057ddb123c172184a44e4e5
}
</style>

<style>
.bp-dropdown {
  margin-left: auto;
}
.bp-dropdown__btn {
  border-radius: 5px;
}
.bp-dropdown__btn--active {
  background-color: transparent;
}
.dropitem {
  margin: 5px;
  padding: 3px;
}

a {
  color: black;
  text-decoration: underline;
}
</style>