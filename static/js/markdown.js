/**
 * Copyright (C) 2020 Lukas Winkler
 *
 * @license magnet:?xt=urn:btih:1f739d935676111cfff4b4693e3816e664797050&dn=gpl-3.0.txt GPL-v3-or-Later
 *
 */

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
});
