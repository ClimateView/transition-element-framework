
document$.subscribe(function() {
    // Dynamic loading of features in order to ensure instant page loading
    // works together with e.g. drawio
    try {
        GraphViewer.processElements();
    } catch (error) {}

    posthog.capture('$pageview');
})

