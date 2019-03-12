from flask import Flask, Blueprint, jsonify

model_controller = Blueprint('model_controller', __name__)

# function for listing all the saved models
@model_controller.route('/', methods=['GET'])
def index():
    items = [
        {"id" : 1, "location" : "files/models/cars.h5py", "name" : "cars"},
        {"id" : 2, "location" : "files/models/goats.h5py", "name" : "goats"},
        {"id" : 3, "location" : "files/models/bananaorcow.h5py", "name" : "bananas or cows"},
    ]

    return jsonify(items)

# function for fetching a single model
@model_controller.route('/<identifier>', methods=['GET'])
def show(identifier):
    model = {"id" : 1, "location" : "files/models/cars.h5py", "name" : "cars"}
    return jsonify(model)

# function for saving a model
@model_controller.route('/', methods=['POST'])
def save():
    return jsonify(success=True)

# function for deleting a model
@model_controller.route('/<identifier>', methods=['DELETE'])
def destroy(identifier):
    return jsonify(success=True)

# function for updating a model
@model_controller.route('/<identifier>', methods=['PUT'])
def update(identifier):
    return jsonify(success=True)