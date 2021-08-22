import bleach
import markdown
from bleach_allowlist import markdown_tags, markdown_attrs


def md_to_html(md: str) -> str:
    html = markdown.markdown(
        md,
        output_format="html",
        extensions=[
            "nl2br",
        ]
    )
    html = bleach.clean(
        html,
        tags=markdown_tags,
        attributes=markdown_attrs
    )
    return html
