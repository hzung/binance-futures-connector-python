#!/usr/bin/env python
import logging
from binance_future.cm_futures import CMFutures as Client
from binance_future.lib.utils import config_logging
from binance_future.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret, base_url="https://dapi.binance.com")

try:
    response = client.balance(recvWindow=6000)
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
