
import { createRouter, createWebHistory } from 'vue-router'
// import Home from './../views/Home.vue'
// import Detail from './../views/Detail.vue'
import NotFound from './../views/404.vue'
// import ListByKind from './../views/ListByKind.vue'
import { defineAsyncComponent } from 'vue';

const routes = [
    {
        path: '/',
        name: 'home',
        component: () => defineAsyncComponent(() =>
            import(/* webpackChunkName: "home" */ './../views/Home.vue')
        )
    },
    {
        path: '/detail',
        name: 'detail',
        component: () => defineAsyncComponent(() =>
            import(/* webpackChunkName: "detail" */ './../views/Detail.vue')
        )
    },
    {
        path: '/the-loai/:name',
        name: 'ListByKind',
        component: () => defineAsyncComponent(() =>
            import(/* webpackChunkName: "ListByKind" */ './../views/ListByKind.vue')
        )
    },
    { 
        path: '/:pathMatch(.*)*', 
        name: 'NotFound', 
        component: () => NotFound 
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;