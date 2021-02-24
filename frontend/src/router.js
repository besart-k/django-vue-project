import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue')
    },
    {
        path: '/about',
        name: 'About',
        component: () => import('@/views/About.vue')
    },
    {
        path: '/risk-types',
        name: 'RiskTypes',
        component: () => import('@/views/RiskTypes.vue')
    },
    {
        path: '/risk-type/:id',
        name: 'RiskType',
        component: () => import('@/views/RiskType.vue'),
        props: true
    },
    {
        path: '/risk-type-add',
        name: 'RiskDefinitionAdd',
        component: () => import('@/views/RiskDefinitionAdd.vue')
    },

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router