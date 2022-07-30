import {InjectCSS, register, ReplaceElements} from '@fortawesome/fontawesome-svg-core/plugins'
import {
    faArrowsAlt,
    faBold,
    faColumns,
    faEye,
    faHeading,
    faImage,
    faItalic,
    faLink,
    faListOl,
    faListUl,
    faQuestionCircle,
    faQuoteLeft
} from '@fortawesome/free-solid-svg-icons'
import {EditorView, minimalSetup} from "codemirror"
import {markdownLanguage} from "@codemirror/lang-markdown"
import {foldGutter} from "@codemirror/language";


const api = register([InjectCSS, ReplaceElements])
api.library.add(
    faBold, faItalic, faHeading, faQuoteLeft, faListUl, faListOl, faLink, faImage,
    faEye, faColumns, faArrowsAlt, faQuestionCircle,
)


const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const ids = ["id_description_md"];
ids.forEach(function (id) {
    const element = document.getElementById(id);
    if (!element) {
        return
    }
    // const ydoc = new Y.Doc()
    // const provider = new WebrtcProvider('some-example-room', ydoc)
    // const ytext = ydoc.getText('codemirror')
    // window.ytext=ytext
    // console.log(ytext.toJSON())
    // const undoManager = new Y.UndoManager(ytext)
    //
    // provider.awareness.setLocalStateField('user', {
    //     name: 'Anonymous ' + Math.floor(Math.random() * 100),
    //     color: "red",
    //     colorLight: "lightred"
    // })

    const div = document.createElement("div")
    element.style.display = "none"
    element.parentElement.insertBefore(div, element)
    const view = new EditorView({
        extensions: [
            minimalSetup,
            foldGutter(),
            markdownLanguage,
            EditorView.lineWrapping,
            EditorView.contentAttributes.of({spellcheck: "true"}),
            // yCollab(ytext, provider.awareness, {undoManager})
        ],
        parent: div,
        doc: element.value,
    })
    element.form.addEventListener("submit", () => {
        element.value = view.state.doc.toString()
    })
    // const easyMDE = new EasyMDE({
    //     element: element,
    //     forceSync: true, // for "required" to work
    //     spellChecker: false,
    //     nativeSpellcheck: true,
    //     autoDownloadFontAwesome: false,
    //     autosave: {
    //         delay: 1000,
    //         submit_delay: 5000,
    //         timeFormat: {
    //             locale: 'de-AT',
    //             format: {
    //                 year: 'numeric',
    //                 month: 'long',
    //                 day: '2-digit',
    //                 hour: '2-digit',
    //                 minute: '2-digit',
    //                 second: '2-digit',
    //             },
    //         },
    //     },
    //     inputStyle: "contenteditable",
    //     status: ["lines", "words", "cursor", "saveStatus"],
    // });
    // window.editor = easyMDE
    // setInterval(function () {
    //     const content = easyMDE.value();
    //     fetch("/api/draft/save", {
    //         method: "POST",
    //         body: JSON.stringify({
    //             "draft_md": content
    //         }),
    //         headers: {'X-CSRFToken': csrftoken},
    //     })
    //         .then(response => response.json())
    //         .then(data => {
    //             easyMDE.updateStatusBar("saveStatus", data.message)
    //             setTimeout(e => easyMDE.updateStatusBar("saveStatus", ""), 5000)
    //         }).catch(e => {
    //         easyMDE.updateStatusBar("saveStatus", "error saving draft")
    //     })
    //
    // }, 1000 * 30)
});
api.dom.i2svg()
