import os
import src.utils.functions as utils
import src.utils.argsparser as myargs

from argparse import Namespace



def test_get_current_time():
    now = utils.get_current_time()
    assert type(now) == float


def test_create_random_key():
    key = utils.create_random_key()
    assert type(key) == str
    assert len(key) == 5


def test_create_random_key_different_length():
    key = utils.create_random_key(8)
    assert type(key) == str
    assert len(key) == 8


def test_is_expired():
    url_time = utils.get_current_time() - 3700
    os.environ["EXIPRATION_TIME"] = "3600"
    is_expired = utils.is_expired(url_time)
    assert is_expired == True


def test_is_not_expired():
    url_time = utils.get_current_time() - 10
    os.environ["EXIPRATION_TIME"] = "3600"
    is_expired = utils.is_expired(url_time)
    assert is_expired == False


def test_build_args():
    args = myargs.build_args()
    assert type(args) == Namespace
