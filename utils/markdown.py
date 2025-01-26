import re
from html.parser import HTMLParser
from typing import Tuple, Set

import bleach
import markdown
from bleach_allowlist import markdown_tags, markdown_attrs

custom_allowed_tags = ["del", "ins"]


def md_to_html(md: str, replacements=None) -> tuple[str, set[str]]:
    md, linked_objects = autolink(md, replacements=replacements)
    html = markdown.markdown(
        md,
        output_format="html",
        extensions=[
            "nl2br",
        ]
    )
    html = bleach.clean(
        html,
        tags=markdown_tags + custom_allowed_tags,
        attributes=markdown_attrs
    )
    return html, linked_objects


def autolink(md: str, replacements=None) -> tuple[str, set[str]]:
    if replacements is None:
        from utils.urls import name2url
        replacements = name2url()
    links = {}
    linked_objects = set()
    i = 0
    for name, (url, obj) in replacements.items():
        regex = r"\bWORD\b".replace("WORD", re.escape(name))
        placeholder = f"SOME{i}LINK"
        md, n_replacements = re.subn(regex, placeholder, md)
        if n_replacements > 0:
            linked_objects.add(obj.graphkey)
        links[placeholder] = f"[{name}]({url})"
        i += 1

    for placeholder, value in links.items():
        md = md.replace(placeholder, value)
    return md, linked_objects


class HTMLFilter(HTMLParser):
    text = ""

    def handle_data(self, data):
        self.text += data


def html_to_text(html: str) -> str:
    f = HTMLFilter()
    f.feed(html)
    return f.text
