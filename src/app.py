from flask import Flask
from flask import request
from flask import Response

import generate_name
import json
import os

app = Flask(__name__)
generate_name.initialize()


@app.route('/name')
def get_name():
    count = min(50, int(request.args.get('count', 1)))
    max_length = int(request.args.get('max-length', 20))
    # print(f'count: {count}  max_length: {max_length}')

    names = generate_name.generate_name(count, max_length)

    names_json = json.dumps(names)

    return Response(names_json, mimetype='application/json')


if __name__ == '__main__':
    flask_host = os.getenv('FLASK_HOST', '0.0.0.0')
    flask_port = int(os.getenv('FLASK_PORT', 4532))
    app.run(debug=True, host=flask_host, port=flask_port)
