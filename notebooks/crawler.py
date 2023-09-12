import sys
sys.path.append('../')

import requests
import threading
import pickle
import argparse

import src
from src.websocket_api import handlers
from src.websocket_api import listeners
import subprocess
import logging
logging.basicConfig(level=logging.INFO)


parser = argparse.ArgumentParser()
parser.add_argument("--item", type=str, required=True)
parser.add_argument("--type", type=str, required=True)


args = parser.parse_args()


ITEM = args.item
TYPE = args.type

def on_message(ws, message):
    result = handlers.handle_channel_message(message)
    timestamp = result['timestamp']
    with open(f'data/{TYPE}/{ITEM}/{timestamp}', 'wb') as f:
        pickle.dump(result, f)
        
def on_error(*args):
    pass

def on_close(*args):
    pass


_thread = threading.Thread(
    target=listeners.get_listener,
    kwargs={
        'on_message': on_message,
        'on_close': on_close,
        'on_error': on_error,
        'event': ITEM,
        'channel': TYPE,
        'time_delay': 1
    }
)
    
_thread.start()