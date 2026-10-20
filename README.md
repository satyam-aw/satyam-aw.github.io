# Satyam Awasthi — Research Portfolio

Source for my [personal website](https://satyam-aw.github.io), featuring research projects, publications, and my CV.

My research focuses on reliable closed-loop brain–computer interfaces: physiological signal acquisition, intended-action decoding, and estimation and control under uncertainty.

## Local development

With Docker running, start the preview from the repository directory:

```bash
docker compose up
```

Open [localhost:8080](http://localhost:8080). Changes to site content are rebuilt automatically.

After changing dependencies or the Dockerfile, rebuild with:

```bash
docker compose up --build
```

To stop the preview:

```bash
docker compose down
```

## Editing the site

- `_pages/`: homepage, CV, and other main pages.
- `_projects/`: project articles and sidebar metadata for resources, publications, keywords, and section navigation.
- `_bibliography/papers.bib`: publication records.
- `_data/`: structured site data.
- `_layouts/`, `_includes/`, and `_sass/`: page layouts, reusable components, and styling.
- `assets/`: images, PDFs, and other media.
- `_config.yml`: site settings.
- `theme-examples/`: archived theme demonstrations, excluded from the published site.

### Pinning projects

Add `pinned: true` to a project's front matter to mark its card with a star. Cards keep their original styling and `importance` order (lower values first). A pinned card stays in a horizontal row if at least 20% of its width is visible at that row's initial scroll position; otherwise, it starts another row within the same category. Unpinned cards continue in the current scrollable row. Rows regroup when the available width changes.

Remove the flag or set it to `false` to unpin. This setting is independent of `selected`, which controls homepage selection. The Projects page keeps the standard 930px container.

See [AGENTS.md](AGENTS.md) for contribution checks and [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for development issues.

## Theme attribution

Built with Jekyll and adapted from [al-folio](https://github.com/alshedivat/al-folio). The original theme license is retained in [LICENSE](LICENSE).
