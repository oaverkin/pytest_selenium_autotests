import os
from config import settings


def get_url():
    if os.getenv('ENV') == 'dev':
        return settings.get('dev').url
    elif os.getenv('ENV') == 'stage':
        return settings.get('stage').url
    elif os.getenv('ENV') == 'prod':
        return settings.get('prod').url


def get_login():
    if os.getenv('ENV') == 'dev':
        return settings.get('dev').login
    elif os.getenv('ENV') == 'stage':
        return settings.get('stage').login
    elif os.getenv('ENV') == 'prod':
        return settings.get('prod').login


def get_password():
    if os.getenv('ENV') == 'dev':
        return settings.get('dev').password
    elif os.getenv('ENV') == 'stage':
        return settings.get('stage').password
    elif os.getenv('ENV') == 'prod':
        return settings.get('prod').password

