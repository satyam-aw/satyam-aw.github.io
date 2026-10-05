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

See [AGENTS.md](AGENTS.md) for contribution checks and [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for development issues.

## Theme attribution

Built with Jekyll and adapted from [al-folio](https://github.com/alshedivat/al-folio). The original theme license is retained in [LICENSE](LICENSE).
