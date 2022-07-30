import 'vite/modulepreload-polyfill'

// import "./scss/main.scss"


import "./js/sentry"
import {default as Dropdown} from 'bootstrap/js/src/dropdown'
import {default as Collapse} from 'bootstrap/js/src/collapse'


const bootstrapModules = [Collapse, Dropdown]

import "./tenantbase"
import "./editor"
