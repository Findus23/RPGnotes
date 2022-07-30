import 'vite/modulepreload-polyfill'

// import "./scss/main.scss"
import "./js/sentry"
import {default as Dropdown} from 'bootstrap/js/src/dropdown'
import {default as Collapse} from 'bootstrap/js/src/collapse'

import "./js/autocomplete"
import "./js/popover"
import "./js/gallery"


const bootstrapModules = [Collapse, Dropdown]

document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById("id_description_md")) {
        import ("./js/codemirror").then(value => console.log("loaded"))
    }
})
