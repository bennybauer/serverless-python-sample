import logging
import requests

log = logging.getLogger()
log.setLevel(logging.DEBUG)

API_HOST = 'https://jsonplaceholder.typicode.com'


def list_posts(event, context):
    """ Retrieve posts list """
    url = API_HOST + '/posts'

    log.debug('calling ' + url)
    res = requests.get(url)

    response = {
        "statusCode": res.status_code,
        "body": res.text
    }

    return response


def get_post(event, context):
    """ Retrieve post by id """
    url = API_HOST + '/posts/' + str(event['pathParameters']['id'])

    log.debug('calling ' + url)
    res = requests.get(url)

    response = {
        "statusCode": res.status_code,
        "body": res.text
    }

    return response
