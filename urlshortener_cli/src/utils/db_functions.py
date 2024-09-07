import utils.functions as utils
from database.db import db

URLS = db['urls'] # create -if not exists - and return urls collection



def get_url_by_target_url(target_url: str) -> dict | None:
    url = URLS.find_one({ "target_url": target_url })
    return url


def get_url_by_key(key: str) -> dict | None:
    url = URLS.find_one({ "key": key })
    return url


def insert_url(target_url: str) -> None:
    url_id = URLS.insert_one({
       'target_url': target_url,
       'key': utils.create_random_key(),
       'shortened_at': utils.get_current_time(),
    }).inserted_id

    if not url_id:
        raise Exception(f'Unable to insert new entry for target url {target_url}')


def update_url(target_url: str, expired: bool) -> None:
    if not expired:
        update = { "$set": { "shortened_at": utils.get_current_time() } }
    else:
        update = { "$set": { "key": utils.create_random_key(), "shortened_at": utils.get_current_time() } }

    new_url = URLS.update_one({ 'target_url': target_url}, update)

    if not new_url.modified_count == 1:
        raise Exception(f'Unable to update entry for target url {target_url}')
