import requests
import logging
import json
from pprint import pprint

from filters.category import category
from filters.location import location
from filters.keywords import keywords
from filters.ranges   import ranges


def pretty_print_POST(req):
    print('{}\n{}\n{}\n\n{}\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
        '------------END------------',
    ))


def prepare_logger(config):
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)

    requests_log.propagate = True

    formatter = logging.Formatter("%(asctime)s %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if "log_file" in config:
        stLogfile = logging.handlers.RotatingFileHandler(
            config["log_file"],
            maxBytes=256*1024,
            backupCount=10
        )
        stLogfile.setFormatter(formatter)
        logger.addHandler(stLogfile)


def generate_payload(config):
    filters = {}
    if "filters" in config:
        filters = config["filters"]
    payload_filters = {
        "enums": {"ad_type":["offer"]},
        "category": category(filters),
        "location": location(filters),
        "keywords": keywords(filters),
        "ranges": ranges(filters),
    }

    limit = 50
    if "limit" in config:
        limit = int(config["limit"])
    payload = {
        "limit": limit,
        "limit_alu": 0,
        "filters": payload_filters
    }

    json_payload =json.dumps(payload)
    return json_payload


def send_request(session, headers, payload):
    req = requests.Request(
        'post',
        'https://api.leboncoin.fr/finder/search',
        headers=headers,
        data=payload
    )

    prepped = req.prepare()
    pretty_print_POST(prepped)
    return session.send(prepped)


def generate_headers(config):
    if config["headers"]:
        return config["headers"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'Accept': '*/*',
        'DNT': '1',
        #'Host': 'api.leboncoin.fr',
        #'Accept-Language': 'en-US,en;q=0.5',
        #'Accept-Encoding': 'gzip, deflate, br',
        #'api_key': 'ba0c2dad52b3ec',
        #'Referer': 'https://www.leboncoin.fr/annonces/offres/centre/', 
        #'Content-Type': 'text/plain;charset=UTF-8',
        #'Origin': 'https://www.leboncoin.fr',
        #'Content-Length': str(len(payload)),
        #'Connection': 'keep-alive',
    }
    return headers


def read_result(r):
    data = r.json()
    if 'ads' in data:
        for ad in data['ads']:
            pprint(ad)
        print("Number of ads: {}".format(len(data['ads'])))


if __name__ == "__main__":
    with open('config.json') as json_file:  
        config = json.load(json_file)
    prepare_logger(config)
    headers = generate_headers(config)
    payload = generate_payload(config) 
    session = requests.Session()
    result = send_request(session, headers, payload)
    if result.status_code == 200:
        read_result(result)
