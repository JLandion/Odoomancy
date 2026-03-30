import datetime
import os
import json

from odoo import fields
from odoo.http import Controller, request, route
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DSDT
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DSDD

from odoo.http import Response

WEBAPP = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'static', 'character-sheet-app'
)

API_ROUTE = '/web/character-sheet/api/%s'

class ManufacturingOrdersWeb(Controller):
    """Controller to dispatch the Character Sheet App."""

    @staticmethod
    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, datetime.datetime):
            return obj.strftime(DSDT)
        if isinstance(obj, datetime.date):
            return obj.strftime(DSDD)

        raise TypeError(f'Type {type(obj)} not serializable')

    @staticmethod
    def get_file(file_path):
        with open(file_path, 'rb') as f:
            return f.read()

    @staticmethod
    def _try_int(value, default=None):
        try:
            return int(value)
        except ValueError:
            return default

    @staticmethod
    def make_response(data, model, _mime='application/json', _status=200):
        if _mime == 'application/json':
            data = json.dumps(data, default=model.json_serial)

            response_headers = [
                ('Access-Control-Allow-Headers', 'Content-Type, Accept'),
                ('Access-Control-Allow-Origin', '*'),
                ('Access-Control-Allow-Credentials', 'true'),
                ('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            ]

            return Response(
                response=data,
                status=_status,
                headers=response_headers,
                mimetype=_mime,
                content_type='%s; charset=utf-8' % _mime
            )

    @route([API_ROUTE % 'app', API_ROUTE % 'app/<path:path>'], auth='user', methods=['GET'], csrf=False, cors='*')
    def app(self, path=''):
        # If the path is empty, serve the index.html
        if not path:
            file_path = os.path.join(WEBAPP, 'index.html')
        else:
            # Construct the file path based on the requested path
            file_path = os.path.join(WEBAPP, path)

            # Check if the file exists, otherwise serve index.html
            if not os.path.exists(file_path):
                file_path = os.path.join(WEBAPP, 'index.html')

        res = self.get_file(file_path)

        return Response(
            response=res,
            status=200,
            mimetype='text/html',
            content_type='text/HTML; charset=utf-8'
        )

