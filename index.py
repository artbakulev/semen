from flask import Flask, request, Response
from datetime import datetime
import json

app = Flask(__name__)

locations = {}


@app.route('/location.send', methods=['POST'])
def location_send():
    data = request.get_json()
    long, lat = data['long'], data['lat']
    locations[datetime.now().isoformat()] = (long, lat)
    return Response(status=200)


@app.route('/location.get', methods=['GET'])
def location_get():
    return Response(json.dumps(locations))


if __name__ == '__main__':
    app.run(debug=True, port='8080')
