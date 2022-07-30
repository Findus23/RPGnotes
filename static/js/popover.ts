// @ts-ignore
import {default as Popover} from "bootstrap/js/src/popover";
// import type {Popover as PopoverType} from "bootstrap";

const popoverTriggerList: NodeListOf<HTMLAnchorElement> = document.querySelectorAll('.content a')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => {
    console.log(popoverTriggerEl.host)
    console.log(popoverTriggerEl.href.startsWith("htt"))
    if (popoverTriggerEl.host !== window.location.host) {
        return
    }
    const popover = new Popover(popoverTriggerEl, {
        content: "test",
        title: "title",
        trigger: 'hover focus',
        placement: "bottom",
        sanitize: false,
        sanitizeFn: (a: string) => a
    });
    popoverTriggerEl.addEventListener('inserted.bs.popover', (e) => {
        console.log("shown")
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
