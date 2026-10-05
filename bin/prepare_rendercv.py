#!/usr/bin/env python3
"""Prepare the website's CV data for RenderCV without changing its source."""

import argparse
import copy
from pathlib import Path
from urllib.parse import urljoin

import yaml


def insert_sections_after(sections, anchor, additions):
    """Insert grouped entries without losing them when the anchor is absent."""
    reordered = {}
    for name, entries in sections.items():
        reordered[name] = entries
        if name == anchor:
            reordered.update(additions)
    if anchor not in sections:
        reordered.update(additions)
    return reordered


def prepare_cv(source, website):
    cv = copy.deepcopy(source["cv"])
    sections = cv.pop("sections", {})
    summary = cv.pop("summary", None)
    label = cv.pop("label", None)
    cv.pop("image", None)
    cv.pop("address", None)
    if summary:
        sections = {"Research Profile": [summary], **sections}
    if label:
        cv["headline"] = label

    for section, entries in sections.items():
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                continue
            if section in ("Skills", "Interests"):
                keywords = entry.get("keywords", [])
                details = ", ".join(keywords) if isinstance(keywords, list) else keywords
                entries[index] = {"label": entry["name"], "details": details}
                continue
            if "studyType" in entry:
                entry["degree"] = entry.pop("studyType")
                if entry.get("score"):
                    entry.setdefault("highlights", []).insert(0, entry.pop("score"))
                if entry.get("courses"):
                    entry.setdefault("highlights", []).append(entry.pop("courses"))
            if section == "Teaching" and "institution" in entry:
                entry["company"] = entry.pop("institution")
            if "authors" in entry:
                entry.pop("publication_type", None)
                if isinstance(entry["authors"], str):
                    entry["authors"] = [name.strip() for name in entry["authors"].split(",")]
                entry["authors"] = [
                    f"**{author}**" if author == cv["name"] else author
                    for author in entry["authors"]
                ]
                if "publisher" in entry:
                    entry["journal"] = entry.pop("publisher")
                if "releaseDate" in entry:
                    entry["date"] = entry.pop("releaseDate")
            if entry.get("url", "").startswith("/"):
                entry["url"] = urljoin(website.rstrip("/") + "/", entry["url"].lstrip("/"))
            # Link descriptive titles without adding a full URL line to the PDF.
            if entry.get("url"):
                if section == "Research Experience":
                    title_field = "company" if entry.get("end_date") == "present" else "position"
                    entry[title_field] = f"[{entry[title_field]}]({entry['url']})"
                elif section == "Selected Research Projects":
                    entry["name"] = f"[{entry['name']}]({entry['url']})"
    research = sections.pop("Research Experience", [])
    if research:
        current = [entry for entry in research if entry.get("end_date") == "present"]
        earlier = [entry for entry in research if entry.get("end_date") != "present"]
        research_sections = {}
        if current:
            research_sections["Current Research Projects"] = current
        if earlier:
            research_sections["Earlier Research Experience"] = earlier
        sections = insert_sections_after(sections, "Education", research_sections)

    publications = sections.pop("Publications", [])
    if publications:
        source_publications = source["cv"]["sections"]["Publications"]
        conference = []
        posters = []
        for entry, source_entry in zip(publications, source_publications):
            if source_entry.get("publication_type") == "workshop_poster":
                posters.append(entry)
            else:
                conference.append(entry)
        publication_sections = {}
        if conference:
            publication_sections["Conference Papers"] = conference
        if posters:
            publication_sections["Workshop and Poster Papers"] = posters
        anchor = "Earlier Research Experience"
        if anchor not in sections:
            anchor = "Current Research Projects"
        sections = insert_sections_after(sections, anchor, publication_sections)
    cv["sections"] = sections
    return {"cv": cv}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--config", type=Path, default=Path("_config.yml"))
    args = parser.parse_args()
    source = yaml.safe_load(args.source.read_text(encoding="utf-8"))
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    website = config["url"].rstrip("/") + "/" + (config.get("baseurl") or "").strip("/")
    prepared = prepare_cv(source, website)
    args.output.write_text(yaml.safe_dump(prepared, allow_unicode=True, sort_keys=False), encoding="utf-8")


if __name__ == "__main__":
    main()
