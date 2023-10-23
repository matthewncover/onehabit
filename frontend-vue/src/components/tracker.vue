<template>
    <div>
        <h3>Tracker</h3>
    </div>
    <v-btn color="primary">Primary Button</v-btn>
    <v-btn color="secondary">Secondary Button</v-btn>
    <v-btn color="accent">Accent Button</v-btn>
    <v-row>
    <!-- Idea 1: Cool Blues -->
    <v-col cols="4">
      <v-card color="primary">
        <v-card-title>Open</v-card-title>
      </v-card>
      <v-card color="secondary">
        <v-card-title>Close</v-card-title>
      </v-card>
      <v-card color="accent">
        <v-card-title>Accent</v-card-title>
      </v-card>
    </v-col>

  </v-row>

</template>

<script>
export default {
    name: "TrackerPage",
}
</script>