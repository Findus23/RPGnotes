import subprocess
import webbrowser
from pathlib import Path
from tempfile import TemporaryDirectory

import jinja2
from django.core.files import File

from campaigns.models import Campaign
from days.models import IngameDay
from rpg_notes.settings import TEMPLATES_DIR

latex_replacements = {}

REPLACE = {
    '\\': '\\textbackslash ',
    '*': '\\textasteriskcentered ',
    '_': '\\_',
    '#': '\\#',
    '$': '\\$',
    '%': '\\%',
    '{': '\\{',
    '}': '\\}',
    '&': '\\&',
    '…': '\\dots ',
    '~': '\\~{}',
    '^': '\\^{}'
}


def latex_escape(text: str) -> str:
    text = text.translate(str.maketrans(REPLACE))
    return text


def md_to_latex(text: str) -> str:
    return latex_escape(text)


env = jinja2.Environment(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%#',
    line_comment_prefix='%%',
    trim_blocks=True,
    autoescape=False,
    loader=jinja2.FileSystemLoader(TEMPLATES_DIR)
)

env.filters['latex-escape'] = env.filters['l'] = latex_escape
env.filters['md'] = md_to_latex


def generate_pdf(data, tenant: Campaign):
    with TemporaryDirectory() as dirname:
        dir = Path(dirname)
        print(dir)
        template = env.get_template('template.tex')
        latex = template.render(data)
        print(latex)
        (dir / "document.tex").write_text(latex)
        out = subprocess.run(["latexmk", "-pdf", "-interaction=batchmode", "document.tex"],
                             cwd=dir, check=False, capture_output=True)
        print(out.stdout.decode())
        if out.returncode != 0:
            print((dir/"document.log").read_text())
            raise RuntimeError("LaTeX failed")
        pdf_file = dir / "document.pdf"
        webbrowser.open(str(pdf_file))
        with pdf_file.open("rb") as f:
            tenant.document.save("document.pdf", File(f))


def create_document(tenant: Campaign):
    data = {"days": IngameDay.objects.all().order_by("-day")}

    generate_pdf(data, tenant)
