import EasyMDE from "easymde";

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


const api = register([InjectCSS, ReplaceElements])
api.library.add(
    faBold, faItalic, faHeading, faQuoteLeft, faListUl, faListOl, faLink, faImage,
    faEye, faColumns, faArrowsAlt, faQuestionCircle,
)

document.addEventListener('DOMContentLoaded', function () {

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const ids = ["id_description_md"];
    ids.forEach(function (id) {
        const element = document.getElementById(id);
        if (!element) {
            return
        }
        const easyMDE = new EasyMDE({
            element: element,
            forceSync: true, // for "required" to work
            spellChecker: false,
            nativeSpellcheck: true,
            autoDownloadFontAwesome: false,
            autosave: {
                delay: 1000,
                submit_delay: 5000,
                timeFormat: {
                    locale: 'de-AT',
                    format: {
                        year: 'numeric',
                        month: 'long',
                        day: '2-digit',
                        hour: '2-digit',
                        minute: '2-digit',
                        second: '2-digit',
                    },
                },
            },
            inputStyle: "contenteditable",
            status: ["lines", "words", "cursor", "saveStatus"],
        });
        window.editor = easyMDE
        setInterval(function () {
            const content = easyMDE.value();
            fetch("/api/draft/save", {
                method: "POST",
                body: JSON.stringify({
                    "draft_md": content
                }),
                headers: {'X-CSRFToken': csrftoken},
            })
                .then(response => response.json())
                .then(data => {
                    easyMDE.updateStatusBar("saveStatus", data.message)
                    setTimeout(e => easyMDE.updateStatusBar("saveStatus", ""), 5000)
                }).catch(e => {
                easyMDE.updateStatusBar("saveStatus", "error saving draft")
            })

        }, 1000 * 30)
    });
    api.dom.i2svg()
});
