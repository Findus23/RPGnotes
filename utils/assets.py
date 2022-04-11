from hashlib import sha256
from pathlib import Path

import sass
from django.core.cache import cache

basedir = Path(__file__).resolve().parent.parent

inputdir = basedir / "static/scss/"
inputfile = inputdir / "main.scss"
outputfile = basedir / "static/css/main.css"
sourcemap = outputfile.with_suffix(".css.map")


def get_file_hash():
    times = 0
    for file in inputdir.glob("*.scss"):
        times += int(file.stat().st_mtime)
        print(times)
    return sha256(times.to_bytes(16, 'little', signed=False)).hexdigest()


def get_css(debug=False):
    sourcemap_name = "css_sourcemap" if debug else str(sourcemap)
    stored_file_hash = cache.get("scss_file_hash")
    real_file_hash = get_file_hash()
    if not stored_file_hash or stored_file_hash != real_file_hash:
        css, sourcemap_text = sass.compile(
            filename=str(inputfile),
            output_style="nested" if debug else "compressed",
            include_paths=[str(inputdir), str(basedir)],
            source_map_filename=sourcemap_name,
            source_map_contents=True
        )
        cache.set("scss_file_hash", real_file_hash)
        cache.set("scss_css", css)
        cache.set("scss_sourcemap", sourcemap_text)
        return css, sourcemap_text

    return cache.get("scss_css"),cache.get("scss_sourcemap")

def save_css():
    css, sourcemap_text = get_css()
    with outputfile.open("w") as f:
        f.write(css)
    with sourcemap.open("w") as f:
        f.write(sourcemap_text)
