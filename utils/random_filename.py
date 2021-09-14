import secrets
import string
from pathlib import Path

alphabet = string.ascii_letters + string.digits


def random_string(letters: int = 32) -> str:
    return ''.join(secrets.choice(alphabet) for i in range(letters))


def get_file_path(instance, filename: str) -> str:
    ext = Path(filename).suffix
    rand = random_string()
    letter = rand[0]
    return f"{letter}/{rand}{ext}"
