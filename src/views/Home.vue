<template>
    <div>
        <header class="bg-white shadow">
            <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
                <h1 class="text-3xl font-bold tracking-tight text-gray-900">Home</h1>
            </div>
        </header>
         <main>
            <div class="mx-auto py-2 sm:px-2 lg:px-2">
                <!-- Your content -->
                <ListManga />
            </div>
        </main>
    </div>
</template>
<script>
export default {
    name: 'home'
}
</script>
<script setup>

import ListManga from './../components/ListManga.vue';

</script>