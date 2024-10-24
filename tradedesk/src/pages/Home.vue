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

    <!-- Dialog -->
    <Dialog title="Title" v-model="showDialog"> Dialog content </Dialog>
  </div>

  <main>
    <h1>MQTTjs VITE Example</h1>
    <p>
      MQTTjs is a simple MQTT client for the browser. It uses WebSockets to
      connect to an MQTT broker.
    </p>
    <p>
      This example uses the public MQTT broker at
      <a href="https://test.mosquitto.org/">test.mosquitto.org</a>.
    </p>
    
    <p>Status: {{ connected ? 'Connected' : 'Disconnected' }}</p>
    <p>
      <button @click="client.publish(pub_topic, payload)">Publish</button>
      <button @click="client.end()">Disconnect</button>
    </p>
    <p>Messages:</p>
    <ul>
      <li v-for="message in messages" :key="message">{{ message }}</li>
    </ul>
    
  </main>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog } from 'frappe-ui'
import { createResource } from 'frappe-ui'
import { session } from '../data/session'
import mqtt from 'mqtt'

const connected = ref(false)
const clientId = 'mqttjs_' + Math.random().toString(16).substring(2, 8)
//const connectUrl = 'ws://192.168.100.80:8008/mqtt'
const connectUrl = 'ws://192.168.100.71:8008/mqtt'
    //const connectUrl = 'wss://broker.emqx.io:8084/mqtt'

    const options = {
      keepalive: 60,
      clientId: clientId,
      clean: true,
      connectTimeout: 30 * 1000,
      /**
       * By default, EMQX allows clients to connect without authentication.
       * https://docs.emqx.com/en/enterprise/v4.4/advanced/auth.html#anonymous-login
       */
      username: 'mqtt',
      password: '',
      reconnectPeriod: 1000,
      // for more options and details, please refer to https://github.com/mqttjs/MQTT.js#mqttclientstreambuilder-options
    }
    const pub_topic = 'account/2103054041/commands'
    const sub_topic = 'account/2103054041/#'
    const payload = '<:HEARTBEAT|HeartBeat:>'
    // https://github.com/mqttjs/MQTT.js#qos
    const qos = 0

    console.log('connecting mqtt client')
    const client = mqtt.connect(connectUrl, options)
//const client = mqtt.connect({path: '/mqtt', host: 'test.mosquitto.org', port: '8008', log: console.log.bind(console),  keepalive: 30,});

const messages = ref([])

client.on("connect", () => {
  console.log("connected");
  connected.value = true
  client.subscribe(sub_topic, (err) => {
    if (!err) {
      console.log("subscribed");
      client.publish(pub_topic, payload);
    }
  });
});

client.on("message", (topic, message) => {
  console.log('message', topic, message.toString());
  // message is Buffer
  messages.value.push(message.toString());
});

client.on("close", () => {
  console.log("close");
  connected.value = false
});


const ping = createResource({
  url: 'ping',
  auto: true,
})

const showDialog = ref(false)
</script>
