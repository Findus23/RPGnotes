const sentryMetaEl = document.getElementById("sentry")

if (sentryMetaEl) {
    import("@sentry/browser").then((Sentry) => {
        console.log(sentryMetaEl)
        Sentry.init({dsn: sentryMetaEl.dataset.dsn});
        Sentry.showReportDialog({eventId: sentryMetaEl.dataset.eventId, lang: sentryMetaEl.dataset.lang});
    })
}

export const test = 1
