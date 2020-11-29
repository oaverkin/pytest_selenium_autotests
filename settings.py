import os


def get_url():
    print("test test test test")
    print(os.getenv('URL'))
    return os.getenv('URL')


def get_login():
    print(os.getenv('LOGIN'))
    return os.getenv('LOGIN')


def get_password():
    print(os.getenv('PASSWORD'))
    return os.getenv('PASSWORD')

