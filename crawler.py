"""

"""

import argparse

from managers.filesystem_managers import local_filesystem_manager, s3_filesystem_manager
from src.websocket_api import handlers
from src.websocket_api import listeners
import logging

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='',
    epilog=''
)

parser.add_argument('channel', type=str, help='')
parser.add_argument('event', type=str, help='')

if __name__ == 'main':

    args = parser.parse_args()
    print(args)

    # def on_message(ws, message):
    #     result = handlers.handle_channel_message(message)
    #
    # def on_error(ws, error):
    #     pass
    #
    # def on_close(ws):
    #     pass
    #
    # listeners.get_listener(
    #     on_message=on_message,
    #     on_close=on_close,
    #     on_error=on_error,
    #     event=args.event,
    #     channel=args.channel
    # )
