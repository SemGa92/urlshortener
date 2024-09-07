import logging
import sys

from argparse import (
    ArgumentParser,
    ArgumentTypeError,
    Namespace,
    )



def _build_args() -> Namespace:
    parser = ArgumentParser(
        prog='URLShortener',
        description='Performs URL shortening and expansion'
        )
    parser.add_argument(
        "-m", "--minify",
        type=str,
        help="Given a complete URL, return a shortened URL"
        )
    parser.add_argument(
        "-e", "--expand",
        type=str,
        help="Given a shortened URL, return the complete URL"
        )

    return parser.parse_args()


def get_args() -> Namespace:
    try:
        args = _build_args()
        if args.minify and args.expand:
            raise ArgumentTypeError(
                "You can use one parameter at a time."
                )
        elif not args.minify and not args.expand:
            raise ArgumentTypeError(
                "You must specify at least one parameter between --minify and --expand."
                )
    except Exception as e:
        logging.error(e)
        sys.exit()

    return args