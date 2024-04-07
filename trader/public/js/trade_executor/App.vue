<script setup>
import { ref } from "vue";

const dynamicMessage = ref("This is the vue ref.");

</script>
<template>
  <div>
	<h3>{{ dynamicMessage }}</h3>
    <h4>Start editing at trader/public/js/trade_executor/App.vue, does tis change when changed</h4>
  </div>

</template>