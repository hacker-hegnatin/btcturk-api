"""

"""

import json
import channel_handlers

commands = {
    100: channel_handlers.channel_result,
    101: channel_handlers.channel_request,
    151: channel_handlers.channel_subscription,
    401: channel_handlers.channel_ticker_all,
    402: channel_handlers.channel_ticker_pair,
    422: channel_handlers.channel_trade_single,
    431: channel_handlers.channel_orderbook_full,
    432: channel_handlers.channel_orderbook_difference
}


def handle_channel_message(raw_message: str = '', **kwargs):

    def _handle_channel_message(raw_data: str = ''):
        data = json.loads(raw_data)
        return data

    message = _handle_channel_message(raw_message)
    channel = message[0]
    result = commands[channel](message, **kwargs)
    return result

