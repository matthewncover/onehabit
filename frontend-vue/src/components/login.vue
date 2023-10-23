<template>
    <div>
        <input v-model="username" placeholder="Username">
        <input v-model="password" placeholder="Password">
        <button @click="login" color="primary">Login</button>
    </div>
</template>

<script>
export default {
    name: "UserLogin",
    data() {
        return {
            username: "",
            password: ""
        };
    },
    methods: {
        async login() {
            const res = await fetch("http://127.0.0.1:8000/login", {
            method: 'POST', 
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username: this.username, password: this.password})});
            const data = await res.json()
            console.log(data);
        }
    }
}
</script>