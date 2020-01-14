from flask import Flask, request, Response
from datetime import datetime
import json

app = Flask(__name__)

locations = []


@app.route('/location.send', methods=['POST'])
def location_send():
    data = request.get_json()
    if not (data.get('long', False) and data.get('lat', False)):
        return Response(status=400)
    with open('input.txt', 'a') as f:
        f.write(str(data))
    long, lat = data['long'], data['lat']
    locations.append((datetime.now().isoformat(), long, lat))
    return Response(status=200)


@app.route('/location.get', methods=['GET'])
def location_get():
    return Response(json.dumps(locations))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5050')
