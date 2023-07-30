"""

"""

import json
import datetime
from datetime import datetime

from src.websocket_api.handlers import _handlers


commands = {
    100: _handlers.channel_result,
    101: _handlers.channel_request,
    151: _handlers.channel_subscription,
    401: _handlers.channel_ticker_all,
    402: _handlers.channel_ticker_pair,
    422: _handlers.channel_trade_single,
    431: _handlers.channel_orderbook_full,
    432: _handlers.channel_orderbook_difference
}


def handle_channel_message(raw_message: str = '', **kwargs):

    storage_connector = kwargs.get('storage_connector', None)

    def _handle_channel_message(_raw_data: str = ''):
        data = json.loads(_raw_data)
        return data

    message = _handle_channel_message(raw_message)
    channel = message[0]

    if channel in commands:
        result = {
            'datetime': datetime.now(),
            'timestamp': datetime.now().timestamp(),
            'message': commands[channel](message, **kwargs),
            'channel': channel
        }
    else:
        result = message

    if storage_connector is not None:
        result = storage_connector(result)

    return result

