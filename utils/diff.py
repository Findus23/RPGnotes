import subprocess
import sys
from difflib import Differ
from tempfile import NamedTemporaryFile


def print_diff_call(str1: str, str2: str, title: str) -> None:
    title = title.replace("/", "")
    with NamedTemporaryFile(delete=True, mode="w", suffix=title) as tmp1:
        with NamedTemporaryFile(delete=True, mode="w", suffix=title) as tmp2:
            tmp1.write(str1)
            tmp1.flush()
            tmp2.write(str2)
            tmp2.flush()
            subprocess.run(["git", "--no-pager", "diff", "--color-words=.", tmp1.name, tmp2.name])


def print_diff(str1: str, str2: str) -> None:
    d = Differ()
    results = d.compare(str1.splitlines(), str2.splitlines())
    sys.stdout.writelines(results)


if __name__ == '__main__':
    print_diff_call("something\nnw", "someting\nnew")
