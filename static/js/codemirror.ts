import {EditorView, minimalSetup} from "codemirror"
import {markdown, markdownLanguage} from "@codemirror/lang-markdown"
import {foldGutter} from "@codemirror/language";
import {
    autocompletion,
    Completion,
    CompletionContext,
    CompletionResult
} from "@codemirror/autocomplete"

interface DraftSaveResponse {
    message: string
}

const csrftoken = (document.querySelector('[name=csrfmiddlewaretoken]')! as HTMLInputElement).value;
const ids = ["id_description_md"];
ids.forEach(function (id) {
    const element = document.getElementById(id) as HTMLTextAreaElement;
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

    interface Element {
        name: string,
        details?: string
    }

    interface HTTPResponse {
        suggestions: Element[]
    }

    let names: Element[] = []
    fetch("/api/suggestions", {})
        .then(response => response.json())
        .then((data: HTTPResponse) => {
            names = data.suggestions
        })

    function myCompletions(context: CompletionContext): CompletionResult | null {
        if (names.length == 0) {
            return null
        }
        let word
        if (!context.explicit) {
            word = context.matchBefore(/@\w*/)

        } else {
            word = context.matchBefore(/\w*/)
        }
        if (!word) {
            return null
        }
        if (word.from == word.to)
            return null

        const options = names.map((s: Element): Completion => ({
            label: "@" + s.name,
            apply: s.name,
            displayLabel: s.name,
            detail: s.details
        }))
        return {
            from: word.from,
            options: options
        }
    }


    const labelEl = element.labels[0]
    const div = document.createElement("div")
    element.style.display = "none"
    element.parentElement!.insertBefore(div, element)
    const view = new EditorView({
        extensions: [
            minimalSetup,
            foldGutter(),
            markdown({base: markdownLanguage}),
            autocompletion({
                activateOnTyping: true,
                override: [myCompletions],
            }),
            EditorView.lineWrapping,
            EditorView.contentAttributes.of({spellcheck: "true"}),
            // yCollab(ytext, provider.awareness, {undoManager})
        ],
        parent: div,
        doc: element.value,
    })
    element.form!.addEventListener("submit", () => {
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
    const originalLabel = labelEl.innerText
    setInterval(function () {
        const content = view.state.doc.toString();
        fetch("/api/draft/save", {
            method: "POST",
            body: JSON.stringify({
                "draft_md": content
            }),
            headers: {'X-CSRFToken': csrftoken},
        })
            .then(response => response.json())
            .then((data: DraftSaveResponse) => {
                labelEl.innerText += ": " + data.message
                setTimeout(() => labelEl.innerText = originalLabel, 5000)
            }).catch(e => {
            labelEl.innerText += ": " + "error saving draft"
        })

    }, 1000 * 30)
})
;
