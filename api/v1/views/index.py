#!/usr/bin/python3
"""module index.py"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def app_view():
    return jsonify({'status': 'ok'})
