from models import storage
from api.v1.views import app_views
from flask import Flask
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext():
    storage.close()

if __name__ == "__main__":
    _host = getenv('HBNB_API_HOST')
    _port = getenv('HBNB_API_PORT')
    if _host == None:
        _host = '0.0.0.0'
    if _port == None:
        _port = 5000
    app.run(host = _host, port = _port, threaded=True)
