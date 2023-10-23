import { createRouter, createWebHistory } from 'vue-router';

import WhyPage from "../components/why.vue"
import TrackerPage from "../components/tracker.vue"
import EditorPage from "../components/editor.vue"
import AnalysisPage from '../components/analysis.vue';

const routes = [
  { path: '/why', component: WhyPage},
  { path: '/tracker', component: TrackerPage},
  { path: '/editor', component: EditorPage},
  { path: '/analysis', component: AnalysisPage}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;