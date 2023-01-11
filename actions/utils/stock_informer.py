import logging
import os
import requests
from urllib.parse import urljoin
from actions.utils import logger

BROKER_API_URL = os.environ['BROKER_API_URL']


class StockInformer:

    @staticmethod
    def get_stock_details(stock_ticker_symbol):
        details_url = urljoin(BROKER_API_URL, f'stocks/details/{stock_ticker_symbol}')
        res = requests.get(details_url)
        if res.status_code == 200:
            return res.json()
        logger.get_root_logger().log(logging.ERROR, 'Failed retrieving stock details.')
        return None

    @staticmethod
    def get_stock_price(stock_ticker_symbol):
        price_url = urljoin(BROKER_API_URL, f'stocks/price/{stock_ticker_symbol}')
        res = requests.get(price_url)
        if res.status_code == 200:
            return res.json()
        logger.get_root_logger().log(logging.ERROR, 'Failed retrieving stock price.')
        return None

if __name__ == '__main__':
    print(StockInformer.get_stock_details('pltr'))
    print(StockInformer.get_stock_price('pltr'))
