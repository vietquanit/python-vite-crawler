<template>
    <div class="fixed bottom-0 right-0 h-16 w-16">
        <svg xmlns="http://www.w3.org/2000/svg" @click="scrollToTop()" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-8 h-8 stroke-1 text-amber-400 border-amber-500 border-2 rounded-full cursor-pointer hover:text-amber-600 hover:stroke-2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l7.5-7.5 7.5 7.5m-15 6l7.5-7.5 7.5 7.5" />
        </svg>
    </div>
</template>
<style scoped>

</style>
<script setup>
const scrollToTop = () => {
    window.scrollTo({
        top: 0,
        behavior:'smooth'
    });
}
</script>