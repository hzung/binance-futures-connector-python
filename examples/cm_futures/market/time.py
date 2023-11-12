#!/usr/bin/env python
import logging
from binance_future.cm_futures import CMFutures
from binance_future.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

cm_futures_client = CMFutures(show_limit_usage=True)

logging.info(cm_futures_client.time())
