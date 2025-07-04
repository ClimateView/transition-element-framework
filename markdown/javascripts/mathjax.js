window.MathJax = {
    loader: {load: ['[tex]/mhchem']},
    tex: {
        packages: {'[+]': ['mhchem']},
        inlineMath: [["\\(", "\\)"], ["$", "$"]],
        displayMath: [["\\[", "\\]"], ["$$", "$$"]],
        processEscapes: true,
        processEnvironments: true
    },
    options: {
        ignoreHtmlClass: ".*",
        processHtmlClass: "arithmatex|md-ellipsis"
    }
};


document$.subscribe(() => {
    try {
        MathJax.startup.output.clearCache()
        MathJax.typesetClear()
        MathJax.texReset()
        MathJax.typesetPromise()
    } catch (error) {}
})



