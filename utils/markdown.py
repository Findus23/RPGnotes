import re

import bleach
import markdown
from bleach_allowlist import markdown_tags, markdown_attrs

custom_allowed_tags = ["del", "ins"]


def md_to_html(md: str) -> str:
    md = autolink(md)
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
    return html


def autolink(md: str) -> str:
    from utils.urls import name2url
    links = {}
    i = 0
    for name, url in name2url().items():
        regex = r"\bWORD\b".replace("WORD", name)
        placeholder = f"SOME{i}LINK"
        md = re.sub(regex, placeholder, md)
        links[placeholder] = f"[{name}]({url})"
        i += 1

    for placeholder, value in links.items():
        md = md.replace(placeholder, value)
    return md
