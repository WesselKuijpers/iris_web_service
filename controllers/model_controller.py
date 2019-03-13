from flask import Flask, Blueprint, jsonify, request
from map_classes.model import Model

model_controller = Blueprint('model_controller', __name__)

# function for listing all the saved models
@model_controller.route('/', methods=['GET'])
def index():
    items = Model().all()
    return jsonify(items)

# function for fetching a single model
@model_controller.route('/<identifier>', methods=['GET'])
def show(identifier):
    model = Model().find_by_id(identifier=identifier)
    return jsonify(model)

# function for saving a model
@model_controller.route('/', methods=['POST'])
def save():
    try:
        if request.form["location"] != "" and request.form["name"] != "":
            new_model = Model(location=request.form["location"], name=request.form["name"])
            result = new_model.save()
        else: 
            result = False
        return jsonify(success=result)
    except:
        return jsonify(succes=False)

# function for deleting a model
@model_controller.route('/<identifier>', methods=['DELETE'])
def destroy(identifier):
    # TODO: finish model destroy funtionality
    return jsonify(success=True)

# function for updating a model
@model_controller.route('/<identifier>', methods=['POST'])
def update(identifier):
    # TODO: finish model update functionality
    return jsonify(success=True)