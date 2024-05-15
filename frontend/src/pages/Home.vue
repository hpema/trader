<template>
  <div class="max-w-3xl py-12 mx-auto">
    <h2 class="font-bold text-lg text-gray-600 mb-4">
      Welcome {{ session.user }}!
    </h2>

    <Button theme="gray" variant="solid" icon-left="code" @click="ping.fetch" :loading="ping.loading">
      Click to send 'ping' request
    </Button>
    <div>
      {{ ping.data }}
      
    </div>
    <pre>{{ ping }}</pre>

    <div class="flex flex-row space-x-2 mt-4">
      <Button @click="showDialog = true">Open Dialog</Button>
      <Button @click="session.logout.submit()">Logout</Button>
    </div>

    <ListView
    class="h-[250px]"
    :columns="[
      {
        label: 'Name',
        key: 'name',
        width: 3,
        getLabel: ({ row }) => row.name,
      },
      {
        label: 'Email',
        key: 'email',
        width: '200px',
      },
      {
        label: 'Role',
        key: 'role',
      },
      {
        label: 'Status',
        key: 'status',
      },
    ]"
    :rows="[
      {
        id: 1,
        name: 'John Doe',
        email: 'john@doe.com',
        status: 'Active',
        role: 'Developer',
        user_image: 'https://avatars.githubusercontent.com/u/499550',
      },
      {
        id: 2,
        name: 'Jane Doe',
        email: 'jane@doe.com',
        status: 'Inactive',
        role: 'HR',
        user_image: 'https://avatars.githubusercontent.com/u/499120',
      },
    ]"
    
    row-key="id"
  >
    <template #cell="{ item, row, column }">
      <span class="font-medium text-gray-700">
        {{ item }}
      </span>
    </template>
  </ListView>
    <div class="space-y-4">
    <div
      class="flex items-center justify-between"
      v-for="trader in traders.data"
      :key="trader.name"
    >
      <div>
        {{ trader.trader_name }}
      </div>
      <Badge>{{ trader.approved }}</Badge>
    </div>
  </div>
  <Button @click="traders.next()"> Next Page </Button>
    <!-- Dialog -->
    <Dialog title="Some thing" v-model="showDialog"> {{ registered_trader.data[1] }} </Dialog>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { createResource } from 'frappe-ui'
import { session } from '../data/session'
import { createDocumentResource } from 'frappe-ui'
import { createListResource } from 'frappe-ui'
import {
  Avatar,
  Dialog,
  ListView,
  ListHeader,
  ListRows,
  ListRow,
  ListRowItem,
  ListSelectBanner,
  ListFooter,
  Dropdown,
  call,
  Tooltip,
} from 'frappe-ui'

const props = defineProps({
  rows: {
    type: Array,
    required: true,
  },
  columns: {
    type: Array,
    required: true,
  },
  options: {
    type: Object,
    default: () => ({
      selectable: true,
      showTooltip: true,
      resizeColumn: false,
      totalCount: 0,
      rowCount: 0,
    }),
  },
})

const emit = defineEmits([
  'loadMore',
  'updatePageCount',
  'columnWidthUpdated',
  'applyFilter',
])

const ping = createResource({
  url: 'ping',
  auto: true,
})

let registered_trader = createDocumentResource({
  doctype:'Registered Trader',
  name: '0681bb54d7'
})

let traders = createListResource({
  doctype: 'Registered Trader',
  fields: ['name','license_key','trader_name','approved'],
  start:0,
  pageLength: 5,
})

traders.fetch()
const showDialog = ref(false)
</script>
