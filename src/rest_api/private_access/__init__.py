"""

"""

import time, base64, hmac, hashlib, requests


def get_account_balance(api_key: str, api_secret: str):

    base = "https://api.btcturk.com"
    method = "/api/v1/users/balances"
    uri = base + method

    api_secret = base64.b64decode(api_secret)

    stamp = str(int(time.time()) * 1000)
    data = "{}{}".format(api_key, stamp).encode("utf-8")
    signature = hmac.new(api_secret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {
        "X-PCK": api_key,
        "X-Stamp": stamp,
        "X-Signature": signature,
        "Content-Type": "application/json"
    }

    result = requests.get(url=uri, headers=headers).json()

    return result


def get_account_orders(api_key: str, api_secret: str, pair: str = 'BTCTRY'):

    base = "https://api.btcturk.com"
    method = f"/api/v1/openOrders?pairSymbol={pair}"
    uri = base + method

    api_secret = base64.b64decode(api_secret)

    stamp = str(int(time.time()) * 1000)
    data = "{}{}".format(api_key, stamp).encode("utf-8")
    signature = hmac.new(api_secret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {
        "X-PCK": api_key,
        "X-Stamp": stamp,
        "X-Signature": signature,
        "Content-Type": "application/json"
    }

    result = requests.get(url=uri, headers=headers).json()

    return result


def submit_order(
    api_key: str,
    api_secret: str,
    pair: str = 'BTCTRY',
    order_method: str = 'market',
    order_type: str = 'sell',
    quantity: float = None,
    price: float = None,
    stop_price: float = 0
):
    """

    :param api_key:
    :param api_secret:
    :param pair:
    :param order_method: "limit", "market", "stoplimit" or "stopmarket"
    :param order_type: "buy" or "sell"
    :param quantity:
    :param price:
    :param stop_price:
    :return:
    """

    base = "https://api.btcturk.com"
    method = "/api/v1/order"
    uri = base + method

    api_secret = base64.b64decode(api_secret)

    stamp = str(int(time.time()) * 1000)
    data = "{}{}".format(api_key, stamp).encode("utf-8")
    signature = hmac.new(api_secret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {
        "X-PCK": api_key,
        "X-Stamp": stamp,
        "X-Signature": signature,
        "Content-Type": "application/json"
    }

    params = {
        "quantity": quantity,
        "price": price,
        "stopPrice": stop_price,
        "newOrderClientId": "STB",
        "orderMethod": order_method,
        "orderType": order_type,
        "pairSymbol": pair
    }

    result = requests.post(url=uri, headers=headers, json=params).json()
    return result


def cancel_order(
    api_key: str,
    api_secret: str,
    order_id: int,
):

    base = "https://api.btcturk.com"
    method = f"/api/v1/order?id={order_id}"
    uri = base + method

    api_secret = base64.b64decode(api_secret)

    stamp = str(int(time.time()) * 1000)
    data = "{}{}".format(api_key, stamp).encode("utf-8")
    signature = hmac.new(api_secret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {
        "X-PCK": api_key,
        "X-Stamp": stamp,
        "X-Signature": signature,
        "Content-Type": "application/json"
    }

    result = requests.delete(url=uri, headers=headers).json()
    return result
