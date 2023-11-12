#!/usr/bin/env python
import time
import logging
from binance_future.lib.utils import config_logging
from binance_future.websocket.cm_futures.websocket_client import CMFuturesWebsocketClient

config_logging(logging, logging.DEBUG)


def message_handler(_, message):
    print(message)


my_client = CMFuturesWebsocketClient(on_message=message_handler)

my_client.book_ticker(
    id=13,
    callback=message_handler,
    symbol="btcusd_perp",
)

time.sleep(10)

logging.debug("closing ws connection")
my_client.stop()
