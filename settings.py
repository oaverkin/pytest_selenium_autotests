import os


def get_url():
    return os.getenv('URL')


def get_login():
    return os.getenv('LOGIN')


def get_password():
    return os.getenv('PASSWORD')

