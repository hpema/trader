import path from 'path'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import frappeui from 'frappe-ui/vite'

export default defineConfig({
  plugins: [vue(), frappeui()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  build: {
    outDir: `../${path.basename(path.resolve('..'))}/public/tradedesk`,
    emptyOutDir: true,
    target: 'es2020',
  },
  optimizeDeps: {
    include: ['feather-icons', 'showdown', 'engine.io-client'],
    force: true,
  },
})