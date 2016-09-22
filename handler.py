# get this file's directory independent of where it's run from
import sys, os

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

API_HOST = 'https://jsonplaceholder.typicode.com'


def list_posts(event, context):
    url = API_HOST + '/posts'

    log.debug('calling ' + url)
    return requests.get(url).json()


def get_post(event, context):
    url = API_HOST + '/posts/' + event['path']['id']

    log.debug('calling ' + url)
    return requests.get(url).json()
