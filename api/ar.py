import json

from flask import jsonify
from flask import make_response
from flask import request

from . import api

ID2OBJ = dict()


@api.route('/ar/objects', methods=['POST'])
def post():
    obj = request.get_json()
    next_id = len(ID2OBJ)
    obj['id'] = next_id
    ID2OBJ[next_id] = obj
    return make_response(jsonify({'id': next_id}), 201)


@api.route('/ar/objects', methods=['GET'])
def get():
    return jsonify(list(ID2OBJ.values()))


@api.route('/ar/objects/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def process(id):
    if request.method == 'DELETE':
        # DELETE
        if id in ID2OBJ:
            del ID2OBJ[id]
        return jsonify({"message": "Object {} deleted successfully".format(id)}), 200
    elif request.method == 'PUT':
        # PUT
        data = request.data
        obj = json.loads(data)
        ID2OBJ[id] = obj
        return jsonify({"message": "Object {} updated successfully".format(id)}), 200
    else:
        # GET
        return jsonify(ID2OBJ[id]), 200
