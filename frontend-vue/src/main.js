import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { loadFonts } from './plugins/webfontloader'
import { createVuetify } from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'


loadFonts()

const app = createApp(App)
const vuetify = createVuetify({
  theme: {
    defaultTheme: 'dark',
    themes: {
      dark: {
        colors: {
          primary: '#afc7d4', // dark navy blue
          secondary: '#295765', // softer navy blue
          accent: '#e6f6bc' // purple
        }
      }
    }
  }
});



app.use(router)
app.use(vuetify)
app.mount('#app')
