#!/usr/bin/env python
import logging
from binance_future.um_futures import UMFutures
from binance_future.lib.utils import config_logging
from binance_future.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

um_futures_client = UMFutures(key=key, secret=secret)

try:
    response = um_futures_client.get_open_orders(
        symbol="BTCUSDT", orderId=35298599362, recvWindow=2000
    )
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
