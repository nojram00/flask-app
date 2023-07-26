from app import app
from waitress import serve
import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
serve(app, host='0.0.0.0', port=8000, _quiet=False, server_name='example.server')

