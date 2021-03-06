import json
from functools import lru_cache
from pathlib import Path
from typing import TypedDict, Dict, List, Optional, Generator

from django.templatetags.static import static
from django_jinja import library

from rpg_notes.settings import STATIC_ROOT


class Asset(TypedDict):
    file: str
    srf: str
    isEntry: bool
    imports: Optional[List[str]]
    isDynamicEntry: Optional[bool]


Manifest = Dict[str, Asset]


@lru_cache()
def load_vite_manifest() -> Manifest:
    with (Path(STATIC_ROOT) / "build" / "manifest.json").open() as f:
        return json.load(f)


@library.global_function
@lru_cache()
def js_asset(entry_point: str) -> Asset:
    manifest = load_vite_manifest()
    try:
        return manifest[entry_point]
    except KeyError:
        return manifest[f"static/{entry_point}"]


@library.global_function
@lru_cache()
def js_asset_url(entry_point: str) -> str:
    asset = js_asset(entry_point)

    return static("build/" + asset["file"])


@library.global_function
def get_dependencies(entry_point: str) -> Generator[Asset, None, None]:
    asset = js_asset(entry_point)
    print(asset)
    if "imports" in asset:
        for imp in asset["imports"]:
            yield from get_dependencies(imp)
    yield static("build/" + asset["file"])
