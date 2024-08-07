import 'vite/modulepreload-polyfill'

// import "./scss/main.scss"
import "./js/sentry"
// @ts-ignore
import Dropdown from 'bootstrap/js/src/dropdown'
// @ts-ignore
import Collapse from 'bootstrap/js/src/collapse'

import "./js/autocomplete"
import "./js/popover"
import "./js/gallery"


const bootstrapModules = [Collapse, Dropdown]

function init(): void {
    if (document.getElementById("id_description_md")) {
        import ("./js/codemirror").then(value => console.log("loaded"))
    }
    if (document.getElementById("graph")) {
        import ("./js/graph").then(value => console.log("graph loaded"))
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init)
} else {
    init()
}
