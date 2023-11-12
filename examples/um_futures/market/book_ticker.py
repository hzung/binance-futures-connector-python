#!/usr/bin/env python
import logging
from binance_future.um_futures import UMFutures
from binance_future.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

um_futures_client = UMFutures()

logging.info(um_futures_client.book_ticker("BTCUSDT"))
