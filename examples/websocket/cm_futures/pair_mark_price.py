#!/usr/bin/env python

import time
import logging
from binance_future.lib.utils import config_logging
from binance_future.websocket.cm_futures.websocket_client import CMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    print(message)


my_client = CMFuturesWebsocketClient(on_message=message_handler)

my_client.pair_mark_price(
    pair="btcusd",
    id=1,
    speed=1,
)

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
