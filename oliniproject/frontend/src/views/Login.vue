<template>
    <div class="login-wrap">
        <form class="block form" @submit.prevent="submitHandler">
            <div class="form__tabs">
                <router-link 
                    tag="button" 
                    to="login"
                    class="form__tabs__tab"
                >
                    Log in
                </router-link>
                <router-link 
                    tag="button" 
                    to="register"
                    class="form__tabs__tab"
                >
                    Sign up
                </router-link>
            </div>

            <!-- EMAIL -->
            <div class="input-field">
                <div v-if="errors.email">
                    <div class="input-field__warn" v-for="(error, key) in errors.email" :key="key">
                        {{error}}
                    </div>
                </div>
                <div class="input-field__warn" v-if="$v.email.$dirty && !$v.email.required">Email is required</div>
                <div class="input-field__warn" v-if="$v.email.$dirty && !$v.email.email">Email format is wrong</div>
                <input 
                    v-model.trim="$v.email.$model" 
                    class="input_styled"
                    :class="{'invalid': !$v.email.email || ($v.email.$dirty && !$v.email.required)}" 
                    type="text" 
                    placeholder="Email">
            </div>

            <!-- PASSWORD -->
            <div class="input-field">
                <div class="input-field__warn" v-if="$v.password.$dirty && !$v.password.required">Password is required</div>
                <div class="input-field__warn" v-if="$v.password.$dirty && !$v.password.minLength">Password has to be {{$v.password.$params.minLength.min}} symbols at least</div>
                <input 
                    v-model.trim="$v.password.$model" 
                    class="input_styled"
                    :class="{'invalid': !$v.password.minLength || ($v.password.$dirty && !$v.password.required)}" 
                    type="password" 
                    placeholder="Password">
            </div>

            <!-- SUBMIT -->
            <div class="form__btn-wrap">
                <button
                    type="submit" 
                    class="waves-effect waves-light btn" 
                    :class="{'button_unactive': false}"
                >
                    {{mode}} 
                    <i class="material-icons right">send</i>
                </button>
            </div>
        </form>
    </div>
</template>

<style lang="css" scoped>
</style>

<script>
import {required, minLength, email} from "vuelidate/lib/validators"
export default {
    data: () => ({
        email: "",
        password: "",
        errors: {}
    }),
    validations: {
        email: {
            required,
            email
        },
        password: {
            required,
            minLength: minLength(3)
        }
    },
    computed: {
        mode() {
            return this.$route.meta.mode;
        }
    },
    methods: {
        resetFields() {
            this.email = "";
            this.password = "";
        },
        submitHandler() {
            if(this.$v.$invalid) {
                this.$v.$touch();
                return;
            }

            let form = {
                user: {
                    email: this.email,
                    password: this.password
                }
            };

            if(this.mode === "log in") {
                this.$store.dispatch("login", form);
            }
            else {
                this.$store.dispatch("register", form)
                .catch(errors => {
                    this.errors = errors;
                    this.resetFields();
                });
            }
        }
    }
}
</script>