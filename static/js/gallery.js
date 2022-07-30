import {LuminousGallery} from "luminous-lightbox";

document.addEventListener('DOMContentLoaded', function () {
    const galleries = document.querySelectorAll("a.image-viewer");
    new LuminousGallery(galleries)
});
