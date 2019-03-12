from flask import Flask, Blueprint, jsonify

predict_controller = Blueprint('predict_controller', __name__)

# function for returning the prediction based on the post data
@predict_controller.route('/', methods=['POST'])
def show():
    # TODO: change stub to actual logic
    prediction = {
        "object" : "car",
        "brand" : "Alfa Romeo",
        "Model" : "Giulia 2.0 BiTurbo TwinSpark",
        "Year" : "2017",
        "Estimate" : "€90000"
    }
    return jsonify(prediction)