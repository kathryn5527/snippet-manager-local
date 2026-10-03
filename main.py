"""Snippet Manager Local — Keep named text snippets in a folder and expand one to stdout or the clipboard."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='snippet_manager_local',
        description='Keep named text snippets in a folder and expand one to stdout or the clipboard.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Snippet Manager Local')
    print('Boilerplate without an editor plugin.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
