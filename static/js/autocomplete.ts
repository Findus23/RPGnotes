import Autocomplete from "@trevoreyre/autocomplete-js"

interface AutocompleteResult {
    url: string
    name: string
    distance: number
}

const form = document.getElementById("autocomplete-form")! as HTMLFormElement

// form.addEventListener("submit", function (e) {
//     e.preventDefault()
// })

new Autocomplete('#autocomplete', {
    search: input => {
        const url = `/search/autocomplete/?q=${encodeURI(input)}`

        return new Promise(resolve => {
            if (input.length === 0) {
                return resolve([])
            }

            fetch(url)
                .then(response => response.json())
                .then((data: AutocompleteResult[]) => {
                    resolve(data)
                })
        })
    },
    getResultValue: (result: AutocompleteResult) => result.name,
    onSubmit: (result: AutocompleteResult) => {
        if (!result) {
            form.submit()
            return
        }
        location.href = result.url
    },
    submitOnEnter: true
})

document.addEventListener("keydown", (event) => {
    const keyName = event.key;
    if (event.ctrlKey && keyName == "k") {
        console.log(keyName)
        const inputEl = form.querySelector("input")
        if (!inputEl) {
            return
        }
        inputEl.focus()
        event.preventDefault()
        return false
    }
})
