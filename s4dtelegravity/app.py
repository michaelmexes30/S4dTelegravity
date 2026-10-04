from __future__ import annotations

import argparse

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="S4dTelegravity")
    parser.add_argument("--name", default="world", help="Name to greet")
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the project version and exit",
    )
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(__version__)
        return 0

    print(f"Hello, {args.name}! S4dTelegravity is ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
