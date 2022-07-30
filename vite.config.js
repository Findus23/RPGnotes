import {defineConfig} from "vite";
import visualizer from "rollup-plugin-visualizer";

export default defineConfig({
    plugins: [
        // splitVendorChunkPlugin(),
        visualizer(),
    ],
    build: {
        outDir: "build_static/build",
        assetsDir: ".",
        // generate manifest.json in outDir
        manifest: true,
        rollupOptions: {
            // overwrite default .html entry
            input: {
                "main": 'static/main.js',
                "tenantbase": 'static/tenantbase.js',
                "editor": 'static/editor.js'
            },
        }
    }
})
