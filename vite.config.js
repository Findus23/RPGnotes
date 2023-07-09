import {defineConfig} from "vite";

export default defineConfig({
    plugins: [
        // splitVendorChunkPlugin(),
        // visualizer(),
    ],
    build: {
        outDir: "static/build",
        assetsDir: ".",
        // generate manifest.json in outDir
        manifest: true,
        rollupOptions: {
            // overwrite default .html entry
            input: {
                "main": 'static/main.ts',
                // "colortheme": 'static/js/colortheme.ts',
                // "tenantbase": 'static/tenantbase.js',
                // "editor": 'static/editor.js'
            },
        }
    }
})
