import logging

from database.db import client
from modes.expander import expand_url
from modes.minifier import minify_url
from utils.argsparser import get_args

logging.basicConfig(format='%(levelname)s | %(message)s')
logging.getLogger().setLevel(logging.INFO)



if __name__ == '__main__':
    args = get_args()

    try:
        if args.minify:
            shortened = minify_url(args.minify)
            logging.info(f"Shortened into {shortened}")
        elif args.expand:
            expanded = expand_url(args.expand)
            logging.info(f"Expanded into {expanded}")
    except Exception as e:
        logging.error(e)
    finally:
        client.close()
