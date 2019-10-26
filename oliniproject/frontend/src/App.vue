<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>|
      <router-link to="/login">Login</router-link>
    </div>
    <router-view />
  </div>
</template>

<style lang="scss">
	@import "~materialize-css/sass/components/color-variables";
	@import "~materialize-css/sass/materialize.scss";
	// @import "./scss/materialize.config.scss";
	@import "./scss/partials/fonts";
	@import "./scss/main";
</style>
