// @ts-check
import { defineConfig } from 'astro/config';

import react from '@astrojs/react';
import vercel from '@astrojs/vercel';

import tailwindcss from '@tailwindcss/vite';

import mdx from '@astrojs/mdx';

// https://astro.build/config
export default defineConfig({
  integrations: [react(), mdx(), vercel()],
  vite: {
    plugins: [tailwindcss()],
    optimizeDeps: {
      include: ['react-is'],
    },
  },
  server: {
    host: '0.0.0.0',
  },
});