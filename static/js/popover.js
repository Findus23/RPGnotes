const popoverTriggerList = document.querySelectorAll('.content a')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => {
    const popover = new bootstrap.Popover(popoverTriggerEl, {
        content: "test",
        title: "title",
        trigger: 'hover focus',
        placement: "bottom",
        sanitize: false,
        sanitizeFn: a => a
    });
    popoverTriggerEl.addEventListener('inserted.bs.popover', (e) => {
        console.log("shown")
        console.log(popoverTriggerEl.href)
        fetch(popoverTriggerEl.href + "?format=json").then(response => response.json())
            .then(data => {
                popover.setContent({
                    '.popover-header': data["name"],
                    '.popover-body': data["description"]
                })
            });
    }, {once: true})

    return popover
})
