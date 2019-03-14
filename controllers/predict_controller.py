from flask import Flask, Blueprint, jsonify, request, abort
from map_classes.model import Model
from helpers import predict_helper

predict_controller = Blueprint('predict_controller', __name__)

# function for returning the prediction based on the post data
@predict_controller.route('/', methods=['POST'])
def show():
    # TODO: change stub to actual logic
    helper = predict_helper.PredictHelper()
    # try:
    model_object = Model().find_by_id(request.form['model_id'])
    model = helper.load_model(model_object['location'])
    # except:
        # abort(404)
    
    image = request.files['image']
    image = helper.reshape_image(image)

    raw_prediction = model.predict_classes(image)

    prediction = []
    for pred in raw_prediction:
        prediction.append(pred.item())
    
    helper.clear_session()

    return jsonify(prediction)