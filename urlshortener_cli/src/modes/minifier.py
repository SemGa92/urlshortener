import logging
import os
import utils.db_functions as db_utils
import utils.functions as utils


def _get_minified(target_url: str) -> str:
    key = db_utils.get_url_by_target_url(target_url)['key']
    return f"{os.getenv('SHORTNER_ENDPOINT')}{key}"


def minify_url(target_url: str) -> str:
    url = db_utils.get_url_by_target_url(target_url)

    if url is not None:
        expired = utils.is_expired(url['shortened_at'])
        if expired:
            logging.warning(f"{target_url} has already been shortened. This new shortened url is now valid for 1 hour from now.")
        db_utils.update_url(target_url, expired)
        logging.info(f"{target_url} correctly update")
    else:
        db_utils.insert_url(target_url)
        logging.info(f"{target_url} correctly inserted")

    return _get_minified(target_url)
