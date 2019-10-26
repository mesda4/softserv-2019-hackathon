<template>
    <div class="account block">
        <!-- ADMIN -->
        <form @submit.prevent="submitHandler" class="account-inner-wrapper" v-if="!user.is_stuff">
            <div class="title">
                <h5>ADMIN</h5>
            </div>

            <div class="title">
                <h6>CREATE PET</h6>
            </div>

            <div class="input-field">
                <!-- <div class="input-field__warn" v-if="$v.email.$dirty && !$v.email.required">Email is required</div> -->
                <!-- <div class="input-field__warn" v-if="$v.email.$dirty && !$v.email.email">Email format is wrong</div> -->
                    <!-- :class="{'invalid': !$v.name.name || ($v.name.$dirty && !$v.name.required)}"  -->
                <input 
                    v-model.trim="$v.name.$model" 
                    class="input_styled"
                    type="text" 
                    placeholder="Name">
            </div>

            <div class="input-field">
                <input 
                    v-model.trim="$v.breed.$model" 
                    class="input_styled"
                    type="text" 
                    placeholder="Breed">
            </div>

            <div class="input-field">
                <input 
                    v-model.trim="$v.description.$model" 
                    class="input_styled"
                    type="text" 
                    placeholder="Description">
            </div>

            <div class="btn-wrapper">
                <button
                    type="submit"
                    class="waves-effect waves-light btn"
                >
                    CREATE PET
                    <i class="material-icons right">keyboard_tab</i>
                </button>
            </div>
        </form>
    </div>
</template>

<script>
import {required} from "vuelidate/lib/validators"

export default {
    data: () => ({
        name: "",
        breed: "",
        description: ""
    }),

    validations: {
        name: {
            required
        },
        breed: {
            required
        },
        description: {
            required
        }
    },

    computed: {
        user() {
            return this.$store.state.auth.user;
        }
    },

    methods: {
        resetFields() {
            this.name = "";
            this.description = "";
            this.breed = "";
        },
        submitHandler() {
            if(this.$v.$invalid) {
                this.$v.$touch();
                return;
            }

            let form = {
                pet: {
                    name: this.name,
                    description: this.description,
                    id_type: this.breed
                }
            };

            this.$store.dispatch("createPet", form);

            this.resetFields();
        }
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