"use strict";(()=>{var o="(prefers-color-scheme: dark)",s=()=>localStorage.getItem("theme"),m=e=>localStorage.setItem("theme",e),i=()=>{let e=s();return e||(window.matchMedia(o).matches?"dark":"light")},n=e=>{e==="auto"&&window.matchMedia(o).matches?document.documentElement.setAttribute("data-bs-theme","dark"):document.documentElement.setAttribute("data-bs-theme",e)};n(i());var c=(e,a=!1)=>{let t=document.getElementById("navbar-main-dropdown");if(!t)return;let r=document.querySelector(`[data-bs-theme-value="${e}"]`);r&&(console.log(r),document.querySelectorAll("[data-bs-theme-value]").forEach(d=>{d.classList.remove("active"),d.setAttribute("aria-pressed","false")}),r.classList.add("active"),r.setAttribute("aria-pressed","true"),a&&t.focus())};window.matchMedia(o).addEventListener("change",()=>{let e=s();e!=="light"&&e!=="dark"&&n(i())});window.addEventListener("DOMContentLoaded",()=>{let e=s();e||(e="auto"),c(e),document.querySelectorAll("[data-bs-theme-value]").forEach(a=>{a.addEventListener("click",()=>{let t=a.getAttribute("data-bs-theme-value");m(t),n(t),c(t,!0)})})});})();
/*!
 * Color mode toggler based on Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2023 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */
//# sourceMappingURL=colortheme.js.map
