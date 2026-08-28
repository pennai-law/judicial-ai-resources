#!/usr/bin/env python3
"""Validate the public portal's repeated evidence and editorial fields."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import sys


USE_CASE_ATTRIBUTES = ("data-use-case", "data-risk", "data-provenance",
                       "data-source-refs", "data-reviewed")
SOURCE_ATTRIBUTES = ("data-source", "data-source-type", "data-reviewed")
USE_CASE_FIELDS = ("failure-mode", "human-check", "authorization")
FORBIDDEN = ("[verify]", "early release", "noindex", "is not yet in hand",
             "safe and effective today")


@dataclass
class Record:
    kind: str
    attributes: dict[str, str]
    line: int
    fields: set[str] = field(default_factory=set)


class PortalParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.records: list[Record] = []
        self._stack: list[Record | None] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {key: value or "" for key, value in attrs}
        record = None
        if "data-use-case" in attributes:
            record = Record("use case", attributes, self.getpos()[0])
            self.records.append(record)
        elif "data-source" in attributes:
            record = Record("source", attributes, self.getpos()[0])
            self.records.append(record)
        self._stack.append(record)
        field_name = attributes.get("data-field")
        if field_name:
            for active in reversed(self._stack):
                if active is not None:
                    active.fields.add(field_name)
                    break

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if self._stack:
            self._stack.pop()


def _parse_date(value: str, label: str, stale_days: int, errors: list[str]) -> None:
    try:
        reviewed = date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label}: invalid data-reviewed date {value!r}")
        return
    age = (date.today() - reviewed).days
    if age > stale_days:
        errors.append(f"{label}: stale review date {value} ({age} days old)")


def verify_files(paths: list[Path], stale_days: int = 365) -> list[str]:
    errors: list[str] = []
    records: list[tuple[Path, Record]] = []
    visible_text: list[tuple[Path, str]] = []

    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path}: cannot read file: {exc}")
            continue
        parser = PortalParser()
        try:
            parser.feed(text)
            parser.close()
        except Exception as exc:  # HTMLParser errors are rare but actionable.
            errors.append(f"{path}: HTML parse failure: {exc}")
        records.extend((path, record) for record in parser.records)
        visible_text.append((path, text.lower()))

    sources: dict[str, tuple[Path, Record]] = {}
    use_cases: dict[str, tuple[Path, Record]] = {}
    for path, record in records:
        required = USE_CASE_ATTRIBUTES if record.kind == "use case" else SOURCE_ATTRIBUTES
        label_id = record.attributes.get(required[0], "<missing>")
        label = f"{path}:{record.line} {record.kind} {label_id!r}"
        for attribute in required:
            if not record.attributes.get(attribute):
                errors.append(f"{label}: missing {attribute}")
        for field_name in (USE_CASE_FIELDS if record.kind == "use case" else ("limitation",)):
            if field_name not in record.fields:
                errors.append(f"{label}: missing data-field={field_name!r}")
        reviewed = record.attributes.get("data-reviewed")
        if reviewed:
            _parse_date(reviewed, label, stale_days, errors)
        collection = use_cases if record.kind == "use case" else sources
        if label_id in collection:
            errors.append(f"{label}: duplicate identifier {label_id!r}")
        else:
            collection[label_id] = (path, record)

    for identifier, (path, record) in use_cases.items():
        for source_id in record.attributes.get("data-source-refs", "").split():
            if source_id not in sources:
                errors.append(f"{path}:{record.line} use case {identifier!r}: unknown source {source_id!r}")

    for path, text in visible_text:
        for marker in FORBIDDEN:
            if marker in text:
                errors.append(f"{path}: forbidden public marker {marker!r}")

    return errors


def main() -> int:
    paths = [Path(value) for value in sys.argv[1:]]
    if not paths:
        print("usage: verify_portal.py FILE [FILE ...]", file=sys.stderr)
        return 2
    errors = verify_files(paths)
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
