from pathlib import Path

import sass

basedir = Path(__file__).resolve().parent.parent.parent

inputdir = basedir / "static/scss/"
inputfile = inputdir / "main.scss"
outputfile = basedir / "static/css/main.css"
sourcemap = outputfile.with_suffix(".css.map")


def get_css(debug=False):
    sourcemap_name = "css_sourcemap" if debug else str(sourcemap)
    css, sourcemap_text = sass.compile(
        filename=str(inputfile),
        output_style="nested" if debug else "compressed",
        include_paths=[str(inputdir), str(basedir)],
        source_map_filename=sourcemap_name,
        source_map_contents=True
    )
    return css, sourcemap_text


def save_css():
    css, sourcemap_text = get_css()
    with outputfile.open("w") as f:
        f.write(css)
    with sourcemap.open("w") as f:
        f.write(sourcemap_text)
