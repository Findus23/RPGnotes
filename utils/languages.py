"""
list of languages supported by postgresql fulltext search

SELECT cfgname FROM pg_ts_config

"""
full_text_languages = [
    "simple",
    "arabic",
    "danish",
    "dutch",
    "english",
    "finnish",
    "french",
    "german",
    "greek",
    "hungarian",
    "indonesian",
    "irish",
    "italian",
    "lithuanian",
    "nepali",
    "norwegian",
    "portuguese",
    "romanian",
    "russian",
    "spanish",
    "swedish",
    "tamil",
    "turkish"
]
full_text_languages_choice = []
for lang in full_text_languages:
    full_text_languages_choice.append((
        lang,
        "Other" if lang == "simple" else lang.title()
    ))
