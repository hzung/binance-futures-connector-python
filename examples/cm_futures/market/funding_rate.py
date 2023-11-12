#!/usr/bin/env python
from binance_future.cm_futures import CMFutures
import logging
from binance_future.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

cm_futures_client = CMFutures()
logging.info(cm_futures_client.funding_rate("BTCUSD_PERP", **{"limit": 100}))
