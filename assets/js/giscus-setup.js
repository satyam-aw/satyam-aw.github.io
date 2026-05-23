(function setupGiscus() {
  const container = document.getElementById("giscus_thread");
  if (!container) return;

  const ds = container.dataset || {};

  function determineGiscusTheme(darkTheme, lightTheme) {
    
    let theme =
      localStorage.getItem("theme") ||
      document.documentElement.getAttribute("data-theme") ||
      "system";

    if (theme === "dark") return darkTheme || "dark";
    if (theme === "light") return lightTheme || "light";

    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    return prefersDark ? (darkTheme || "dark") : (lightTheme || "light");
    
  }

  let giscusTheme = determineGiscusTheme(ds.darkTheme, ds.lightTheme);

  let giscusAttributes = {
    src: "https://giscus.app/client.js",
    "data-repo": ds.repo || "satyam-aw/satyam-aw.github.io",
    "data-repo-id": ds.repoId || "R_kgDOG3tAmA",
    "data-category": ds.category || "General",
    "data-category-id": ds.categoryId || "DIC_kwDOG3tAmM4C9r7E",
    "data-mapping": ds.mapping || "pathname",
    "data-strict": ds.strict || "1",
    "data-reactions-enabled": ds.reactionsEnabled || "1",
    "data-emit-metadata": ds.emitMetadata || "0",
    "data-input-position": ds.inputPosition || "bottom",
    "data-theme": giscusTheme,
    "data-lang": ds.lang || "en",
    crossorigin: "anonymous",
    async: true,
  };

  let giscusScript = document.createElement("script");
  Object.entries(giscusAttributes).forEach(([key, value]) =>
    giscusScript.setAttribute(key, value)
  );
  container.appendChild(giscusScript);
})();

