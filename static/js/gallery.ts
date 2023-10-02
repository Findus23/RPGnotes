import {LuminousGallery} from "luminous-lightbox";

function initGallery(): void {
    const galleries = document.querySelectorAll("a.image-viewer");
    new LuminousGallery(galleries)
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGallery)
} else {
    initGallery()
}
