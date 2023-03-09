import argparse
import re
import sys
from typing import Sequence

from git import Repo


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regex", action='append', help="Regex for branch name checking")
    args = parser.parse_args(argv)

    active_branch = Repo().head.ref.name
    compiled_regex = re.compile(args.regex[0])

    exit_code = 0
    if compiled_regex.match(active_branch) is None:
        exit_code = 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
