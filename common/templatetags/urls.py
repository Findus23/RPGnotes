from django_jinja import library

from rpg_notes.settings import DEBUG, DOMAIN


@library.global_function
def main_url():
    protocol = "http" if DEBUG else "https"
    return f"{protocol}://{DOMAIN}"
