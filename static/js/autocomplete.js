new Autocomplete('#autocomplete', {
    search: input => {
        const url = `/search/autocomplete/?q=${encodeURI(input)}`

        return new Promise(resolve => {
            if (input.length === 0) {
                return resolve([])
            }

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    resolve(data)
                })
        })
    },
    getResultValue: result => result.name,
    onSubmit: result => {
        if (!result) {
            return
        }
        location.href = result.url
    }

})
