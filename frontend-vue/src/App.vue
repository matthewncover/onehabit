<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
    <v-navigation-drawer app>
    <v-list>
      <v-list-item-group>
        <v-list-item v-for="route in routes" :key="route.path" :to="route.path">
          <v-row no-gutters>
            <v-col cols="auto" class="pr-4">
              <v-list-item-icon>
                <v-icon>{{ route.icon }}</v-icon>
              </v-list-item-icon>
            </v-col>
            <v-col>
              <v-list-item-content>
                <v-list-item-title>{{ route.name }}</v-list-item-title>
              </v-list-item-content>
            </v-col>
          </v-row>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data() {
    return {
      routes: [
        { path: '/why', name: 'Why', icon: 'mdi-home' },
        { path: '/tracker', name: 'Tracker', icon: 'mdi-check-all' },
        { path: '/editor', name: 'Editor', icon: 'mdi-format-align-left' },
        { path: '/analysis', name: 'Analysis', icon: 'mdi-chart-bar' },
      ],
    };
  },
}

</script>
