/*!
 * Color mode toggler based on Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2023 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

const darkQuery='(prefers-color-scheme: dark)'

const getStoredTheme = () => localStorage.getItem('theme')
const setStoredTheme = (theme: string) => localStorage.setItem('theme', theme)

const getPreferredTheme = () => {
    const storedTheme = getStoredTheme()
    if (storedTheme) {
        return storedTheme
    }

    return window.matchMedia(darkQuery).matches ? 'dark' : 'light'
}

const setTheme = (theme: string) => {
    if (theme === 'auto' && window.matchMedia(darkQuery).matches) {
        document.documentElement.setAttribute('data-bs-theme', 'dark')
    } else {
        document.documentElement.setAttribute('data-bs-theme', theme)
    }
}

setTheme(getPreferredTheme())

const showActiveTheme = (theme: string, focus: boolean = false) => {
    const themeSwitcher = document.getElementById("navbar-main-dropdown")
    if (!themeSwitcher) {
        return
    }

    const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`)
    if (!btnToActive) {
        return
    }
    console.log(btnToActive)

    document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
        element.classList.remove('active')
        element.setAttribute('aria-pressed', 'false')
    })

    btnToActive.classList.add('active')
    btnToActive.setAttribute('aria-pressed', 'true')

    if (focus) {
        themeSwitcher.focus()
    }
}

window.matchMedia(darkQuery).addEventListener('change', () => {
    const storedTheme = getStoredTheme()
    if (storedTheme !== 'light' && storedTheme !== 'dark') {
        setTheme(getPreferredTheme())
    }
})

window.addEventListener('DOMContentLoaded', () => {
    let showTheme = getStoredTheme()
    if (!showTheme) {
        showTheme = "auto"
    }
    showActiveTheme(showTheme)

    document.querySelectorAll('[data-bs-theme-value]')
        .forEach(toggle => {
            toggle.addEventListener('click', () => {
                const theme = toggle.getAttribute('data-bs-theme-value')!
                setStoredTheme(theme)
                setTheme(theme)
                showActiveTheme(theme, true)
            })
        })
})
