"""

"""

import requests


def get_exchange_info():
    base = "https://api.btcturk.com"
    method = "/api/v2/server/exchangeinfo"
    uri = base + method
    result = requests.get(url=uri).json()
    return result


def get_pair_info(pair: str = 'BTCUSDT'):
    base = "https://api.btcturk.com"
    method = f"/api/v2/ticker?pairSymbol={pair}"
    uri = base + method
    result = requests.get(url=uri).json()
    return result


def get_all_pairs_info():
    return get_pair_info(pair='')


def get_orderbook(pair: str = 'BTCTRY', limit: int = 25):
    base = "https://api.btcturk.com"
    method = f"/api/v2/orderbook?pairSymbol={pair}&limit={limit}"
    uri = base + method

    result = requests.get(url=uri).json()
    return result


def get_trades(pair: str = 'BTCTRY', limit: int = 25):
    base = "https://api.btcturk.com"
    method = f"/api/v2/trades?pairSymbol={pair}&last={limit}"
    uri = base + method

    result = requests.get(url=uri).json()
    return result


def get_ohlcs(pair: str = 'BTCTRY', start_time: int = -1, end_time: int = -1):
    """
    !!!DAILY
    :param pair:
    :param start_time:
    :param end_time:
    :return:
    """
    base = "https://graph-api.btcturk.com"
    if start_time == -1 or end_time == -1:
        method = f"/v1/ohlcs?pair={pair}"
    else:
        method = f"/v1/ohlcs?pair={pair}&from={start_time}&to={end_time}"
    uri = base + method
    result = requests.get(url=uri).json()
    return result


def get_klines(pair: str = 'BTCTRY', start_time: int = 1688845600, end_time: int = 1694029600, resolution: str = "1"):
    """

    :param pair:
    :param start_time:
    :param end_time:
    :param resolution: 1, 15, 30, 60, 240, 1d, 1w
    :return:
    """

    base = "https://graph-api.btcturk.com"
    if start_time == -1 or end_time == -1:
        method = f"/v1/klines/history?symbol={pair}"
    else:
        method = f"/v1/klines?symbol={pair}&from={start_time}&to={end_time}&resolution={resolution}"
    uri = base + method
    result = requests.get(url=uri).json()
    return result
