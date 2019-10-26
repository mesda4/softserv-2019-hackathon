<template>
    <div class="account block">
        <div class="title">
            <h5>Account</h5>
        </div>

        <div class="account-inner-wrapper">
            <div class="info">
                <div>First name</div>
                <div>{{user.first_name || "No first name"}}</div>
            </div>
            <div class="info">
                <div>Last name</div>
                <div>{{user.last_name || "No first name"}}</div>
            </div>
        </div>

        <!-- <div class="btn-wrapper">
            <button
                @click="editAccount()"
                class="waves-effect waves-light btn"
            >
                EDIT ACCOUNT
                <i class="material-icons right">create</i>
            </button>
        </div> -->
        <!-- ADMIN -->
        <div v-if="!user.is_stuff">
            <div class="btn-wrapper">
                <router-link
                    to="/adminPanel"
                    tag="button"
                    class="waves-effect waves-light btn"
                >
                    ADMIN PANEL
                    <i class="material-icons right">keyboard_tab</i>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    computed: {
        user() {
            return this.$store.state.auth.user;
        }
    },

    created() {
        this.$store.dispatch("getUser");
    }
}
</script>

<style lang="scss" scoped>
.account {
    margin: 0 auto;
    width: 450px;
}

.account-inner-wrapper {
    padding: 0 1rem;
}

.btn-wrapper {
    text-align: center;
    margin: 1.5rem 0;
}
</style>