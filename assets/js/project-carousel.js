// Keep important cards discoverable without expanding the standard reading lane.
(() => {
  const minimumPeek = 0.2;

  function initialize() {
    document.querySelectorAll("[data-project-carousel]").forEach((wrapper) => {
      const originalRow = wrapper.querySelector(".project-carousel");
      const cards = Array.from(originalRow.children);
      const previousButton = wrapper.querySelector('[data-direction="-1"]');
      const nextButton = wrapper.querySelector('[data-direction="1"]');
      const category = wrapper.dataset.category;
      let extraRows = [];
      let lastWidth = 0;
      let frame = null;

      function setUpRow(rowWrapper, row, items, index) {
        row.replaceChildren(...items);
        row.scrollLeft = 0;
        row.dataset.count = items.length;
        row.setAttribute("aria-label", `${category} projects, row ${index + 1}`);
        const overflows = row.scrollWidth > row.clientWidth + 1;
        rowWrapper.querySelectorAll(".carousel-btn").forEach((button) => {
          button.style.display = overflows ? "" : "none";
          button.setAttribute("aria-controls", row.id);
        });
      }

      function layoutRows() {
        frame = null;
        const width = originalRow.clientWidth;
        if (!width || Math.abs(width - lastWidth) < 0.5) return;
        lastWidth = width;

        // Move the existing cards, preserving their images, links, and event handlers.
        originalRow.replaceChildren(...cards);
        originalRow.scrollLeft = 0;
        extraRows.forEach((row) => row.remove());
        extraRows = [];
        const gap = parseFloat(getComputedStyle(originalRow).gap) || 0;
        const measurements = cards.map((item) => {
          const slot = item.getBoundingClientRect();
          const card = item.querySelector(".card").getBoundingClientRect();
          return { item, width: slot.width, inset: card.left - slot.left, cardWidth: card.width };
        });
        const groups = [[]];
        let offset = 0;
        measurements.forEach(({ item, width: slotWidth, inset, cardWidth }) => {
          const visible = Math.max(0, Math.min(cardWidth, width - offset - inset));
          if (item.dataset.pinned === "true" && groups.at(-1).length && visible + 0.01 < cardWidth * minimumPeek) {
            groups.push([]);
            offset = 0;
          }
          groups.at(-1).push(item);
          offset += slotWidth + gap;
        });

        setUpRow(wrapper, originalRow, groups[0], 0);
        let preceding = wrapper;
        groups.slice(1).forEach((items, index) => {
          const rowWrapper = wrapper.cloneNode(false);
          rowWrapper.removeAttribute("data-project-carousel");
          const row = originalRow.cloneNode(false);
          row.id = `${originalRow.id}-row-${index + 2}`;
          rowWrapper.append(previousButton.cloneNode(true), row, nextButton.cloneNode(true));
          preceding.after(rowWrapper);
          setUpRow(rowWrapper, row, items, index + 1);
          extraRows.push(rowWrapper);
          preceding = rowWrapper;
        });
      }

      function scheduleLayout() {
        if (frame === null) frame = requestAnimationFrame(layoutRows);
      }

      layoutRows();
      if (typeof ResizeObserver !== "undefined") {
        new ResizeObserver(scheduleLayout).observe(originalRow);
      } else {
        window.addEventListener("resize", scheduleLayout);
      }
    });

    document.querySelector(".projects")?.addEventListener("click", (event) => {
      const button = event.target.closest(".carousel-btn");
      if (!button) return;
      const row = button.closest(".carousel-wrapper").querySelector(".project-carousel");
      const card = row.querySelector(".carousel-card-item");
      const gap = parseFloat(getComputedStyle(row).gap) || 0;
      const distance = card ? card.getBoundingClientRect().width + gap : row.clientWidth;
      row.scrollBy({ left: Number(button.dataset.direction) * distance, behavior: "smooth" });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize, { once: true });
  } else {
    initialize();
  }
})();
