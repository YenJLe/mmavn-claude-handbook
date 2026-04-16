"""Colour the last word of the site name (Handbook) gold in the top header.

MkDocs Material renders site_name as plain text inside a span, so we cannot
add inline markup via config. This hook runs after each page is rendered and
rewrites the first occurrence (the header) only, leaving <title>, meta tags,
breadcrumbs, and page content untouched.
"""
from __future__ import annotations

import re

_PATTERN = re.compile(
    r'<span class="md-ellipsis">\s*MMA Vietnam Claude Handbook\s*</span>',
    flags=re.DOTALL,
)

_REPLACEMENT = (
    '<span class="md-ellipsis">'
    'MMA Vietnam Claude '
    '<span class="handbook-accent">Handbook</span>'
    '</span>'
)


def on_post_page(output: str, **kwargs) -> str:
    return _PATTERN.sub(_REPLACEMENT, output, count=1)
