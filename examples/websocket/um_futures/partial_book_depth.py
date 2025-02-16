#!/usr/bin/env python

import time
import logging
from binance_future.lib.utils import config_logging
from binance_future.websocket.um_futures.websocket_client import UMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(message):
    print(message)


my_client = UMFuturesWebsocketClient(on_message=message_handler)

my_client.partial_book_depth(
    symbol="bnbusdt",
    id=1,
    level=10,
    speed=100,
)

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
