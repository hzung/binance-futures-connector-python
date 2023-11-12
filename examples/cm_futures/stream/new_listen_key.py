#!/usr/bin/env python
import logging
from binance_future.cm_futures import CMFutures
from binance_future.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

cm_futures_client = CMFutures(key=key)

logging.info(cm_futures_client.new_listen_key())
