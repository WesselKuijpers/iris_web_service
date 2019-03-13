from flask import Flask, Blueprint, jsonify, request
from map_classes.model import Model
from helpers import predict_helper

predict_controller = Blueprint('predict_controller', __name__)

# function for returning the prediction based on the post data
@predict_controller.route('/', methods=['POST'])
def show():
    # TODO: change stub to actual logic
    model = Model().find_by_id(request.form['model_id'])
    helper = predict_helper.PredictHelper()
    file = helper.load_model(model['location'])
    
    prediction = {
        "object" : "car",
        "brand" : "Alfa Romeo",
        "Model" : "Giulia 2.0 BiTurbo TwinSpark",
        "Year" : "2017",
        "Estimate" : "€90000"
    }
    return jsonify(prediction)