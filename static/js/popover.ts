// @ts-ignore
import {default as Popover} from "bootstrap/js/src/popover";
import type {Popover as PopoverType} from "bootstrap";
import {PopoverResponse} from "../types/own";

const popoverTriggerList: NodeListOf<HTMLAnchorElement> = document.querySelectorAll('.content a')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => {
    console.log(popoverTriggerEl.host)
    console.log(popoverTriggerEl.href.startsWith("htt"))
    if (popoverTriggerEl.host !== window.location.host) {
        return
    }
    const popover: PopoverType = new Popover(popoverTriggerEl, {
        content: "test",
        title: "title",
        trigger: 'hover focus',
        placement: "bottom",
        sanitize: true,
        html: true,
        template: '<div class="popover" role="tooltip">' +
            '<div class="popover-arrow"></div>' +
            '<h3 class="popover-header"></h3>' +
            '<div class="popover-image"></div>' +
            '<div class="popover-body"></div>' +
            '</div>',
    });
    popoverTriggerEl.addEventListener('inserted.bs.popover', (e) => {
        console.log("shown")
        fetch(popoverTriggerEl.href + "?format=json").then(response => response.json())
            .then((data: PopoverResponse) => {
                const content :{ [el: string]: string } ={
                    '.popover-header': data.name,
                    '.popover-body': data.description
                }
                if (data.image) {
                    const img = document.createElement("img")
                    img.src = data.image
                    img.style.width="100%"
                    content[".popover-image"] = img.outerHTML;
                }
                popover.setContent(content)
            });
    }, {once: true})

    return popover
})
