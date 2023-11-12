#!/usr/bin/env python
import logging
from binance_future.cm_futures import CMFutures
from binance_future.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

cm_futures_client = CMFutures()

logging.info(
    cm_futures_client.top_long_short_position_ratio("BTCUSD", "1h", **{"limit": 30})
)
