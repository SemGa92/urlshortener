import utils.db_functions as db_utils
import utils.functions as utils


def _get_key(shortened_url: str) -> str:
    return shortened_url.split('/')[-1]


def expand_url(shortened_url: str) -> str:
    key = _get_key(shortened_url)
    url = db_utils.get_url_by_key(key)

    if url is not None:
        expired = utils.is_expired(url['shortened_at'])
        if expired:
            raise Exception(f"{shortened_url} is expired, please minify the target url again.")
    else:
        raise Exception(f"{shortened_url} does not exist.")

    return url['target_url']
