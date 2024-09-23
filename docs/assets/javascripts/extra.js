/**
 * Observe system color scheme preference changes and update color palette accordingly.
 */
const systemPreferenceObserver = e => {
    const body = document.querySelector("body");
    const currentScheme = body.getAttribute("data-md-color-scheme");
    const autoMode = localStorage.getItem("data-md-color-scheme") === "auto";

    if (autoMode) {
        body.setAttribute("data-md-color-scheme", e.matches ? "slate" : "fraunhofer");
    } else if (currentScheme !== "fraunhofer" && currentScheme !== "slate") {
        // If not explicitly set to light or dark, default to auto behavior
        body.setAttribute("data-md-color-scheme", e.matches ? "slate" : "fraunhofer");
    }
}

const matchListener = window.matchMedia("(prefers-color-scheme: dark)");
matchListener.addListener(systemPreferenceObserver);

// Function to set initial color scheme
const setInitialColorScheme = () => {
    const body = document.querySelector("body");
    const storedScheme = localStorage.getItem("data-md-color-scheme");

    if (storedScheme === "auto" || storedScheme === null) {
        const isDarkMode = matchListener.matches;
        body.setAttribute("data-md-color-scheme", isDarkMode ? "slate" : "fraunhofer");
        localStorage.setItem("data-md-color-scheme", "auto");
    } else {
        body.setAttribute("data-md-color-scheme", storedScheme);
    }
}

// Call setInitialColorScheme when the DOM is fully loaded
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setInitialColorScheme);
} else {
    setInitialColorScheme();
}

// Override the default palette toggle behavior
document.addEventListener("DOMContentLoaded", () => {
    const toggles = document.querySelectorAll(".md-header__option");
    toggles.forEach(toggle => {
        toggle.addEventListener("click", () => {
            const currentScheme = document.body.getAttribute("data-md-color-scheme");
            let newScheme;

            if (currentScheme === "fraunhofer") {
                newScheme = "slate";
            } else if (currentScheme === "slate") {
                newScheme = "auto";
            } else {
                newScheme = "fraunhofer";
            }

            document.body.setAttribute("data-md-color-scheme", newScheme);
            localStorage.setItem("data-md-color-scheme", newScheme);

            if (newScheme === "auto") {
                systemPreferenceObserver(matchListener);
            }
        });
    });
});