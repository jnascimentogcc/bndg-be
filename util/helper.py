import json

from dotenv import load_dotenv
from flask import Response

load_dotenv()


class ResponseHelper:
    def __init__(self, _code=200, _msg=''):
        self.code = _code
        self.msg = _msg
        self._data = {}

    def set_data(self, _data):
        self._data = _data

    def set_code_message(self, _code=200, _msg=''):
        self.code = _code
        self.msg = _msg

    def get_response(self, _secure_token=False, _refresh_token=None):
        dict_response = {
            "code": self.code,
            "message": self.msg,
            "data": self._data,
        }
        _resp = Response(response=json.dumps(dict_response), status=200, mimetype='application/json')
        if _secure_token:
            _resp.set_cookie(key='refreshToken',
                             value=_refresh_token,
                             httponly=True,
                             secure=True,
                             samesite='Strict',
                             max_age=7 * 24 * 60 * 60,
                             path='/')
        return _resp
