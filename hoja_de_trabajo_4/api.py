import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

from flask import Flask, request, jsonify
from body_controller import BodyController
from body_model import BodyModel

app = Flask(__name__)
bc = BodyController()

class Asteroid:

    @app.route('/add_body', methods=['POST'])
    def add_body():
        data = request.json
        new_body = BodyModel(data.get('bodyId'), data.get('englishName'), data.get('isPlanet'), data.get('gravity'), data.get('discoveredBy'), data.get('discoveryDate'), data.get('density'))

        bc.insert_body(new_body)

        body_dict = new_body.to_dict()

        return jsonify({'message': body_dict})

    @app.route('/get_body', methods=['GET'])
    def get_body():
        bodyId = request.args.get('id')

        body_finded = bc.get_body(int(bodyId))

        if body_finded is None:
            body_dict = None
        else:
            body_dict = body_finded.to_dict()

        return jsonify({'message': body_dict})

    @app.route('/get_bodies', methods=['GET'])
    def get_asteroids():
        bc.inorden()

        return jsonify({'message': 'GET METHOD'})

    @app.route('/delete_asteroid', methods=['DELETE'])
    def delete_asteroid():
        return jsonify({'message': 'DELETE METHOD'})

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=3000)
