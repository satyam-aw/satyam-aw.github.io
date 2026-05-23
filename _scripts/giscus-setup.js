---
permalink: /assets/js/giscus-setup.js
---

(function setupGiscus() {
  const container = document.getElementById("giscus_thread");
  if (!container) return;

  const ds = container.dataset || {};

  function determineGiscusTheme(darkTheme, lightTheme) {
    {% if site.enable_darkmode %}
    let theme =
      localStorage.getItem("theme") ||
      document.documentElement.getAttribute("data-theme") ||
      "system";

    if (theme === "dark") return darkTheme || "{{ site.giscus.dark_theme }}";
    if (theme === "light") return lightTheme || "{{ site.giscus.light_theme }}";

    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    return prefersDark ? (darkTheme || "{{ site.giscus.dark_theme }}") : (lightTheme || "{{ site.giscus.light_theme }}");
    {% else %}
    return lightTheme || "{{ site.giscus.light_theme }}";
    {% endif %}
  }

  let giscusTheme = determineGiscusTheme(ds.darkTheme, ds.lightTheme);

  let giscusAttributes = {
    src: "https://giscus.app/client.js",
    "data-repo": ds.repo || "{{ site.giscus.repo }}",
    "data-repo-id": ds.repoId || "{{ site.giscus.repo_id }}",
    "data-category": ds.category || "{{ site.giscus.category }}",
    "data-category-id": ds.categoryId || "{{ site.giscus.category_id }}",
    "data-mapping": ds.mapping || "{{ site.giscus.mapping }}",
    "data-strict": ds.strict || "{{ site.giscus.strict }}",
    "data-reactions-enabled": ds.reactionsEnabled || "{{ site.giscus.reactions_enabled }}",
    "data-emit-metadata": ds.emitMetadata || "{{ site.giscus.emit_metadata }}",
    "data-input-position": ds.inputPosition || "{{ site.giscus.input_position }}",
    "data-theme": giscusTheme,
    "data-lang": ds.lang || "{{ site.giscus.lang }}",
    crossorigin: "anonymous",
    async: true,
  };

  let giscusScript = document.createElement("script");
  Object.entries(giscusAttributes).forEach(([key, value]) =>
    giscusScript.setAttribute(key, value)
  );
  container.appendChild(giscusScript);
})();

