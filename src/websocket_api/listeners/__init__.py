import json
import time
import websocket

try:
    import thread
except ImportError:
    import _thread as thread

channels = ["ticker", "trade", "orderbook", "obdiff"]


def prepare_channel(**kwargs):
    channel = kwargs.get('channel', 'orderbook')
    event = kwargs.get('event', 'BTCTRY')

    message = [
        151,
        {
            "type": 151,
            "channel": channel,
            "event": event,
            "join": True
        }
    ]
    return message


def get_listener(
        on_message: callable = None,
        on_error: callable = None,
        on_close: callable = None,
        **kwargs
):
    time_delay = kwargs.get('time_delay', 3)

    def on_open(stream):
        def _run(*_):
            time.sleep(time_delay)
            message = prepare_channel(**kwargs)
            stream.send(json.dumps(message))

        thread.start_new_thread(_run, ())

    listening_url = 'wss://ws-feed-pro.btcturk.com/'
    ws = websocket.WebSocketApp(
        listening_url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()
