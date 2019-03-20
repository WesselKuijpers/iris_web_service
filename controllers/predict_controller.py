from flask import Flask, Blueprint, jsonify, request, abort
from map_classes.model import Model
from helpers import predict_helper

predict_controller = Blueprint('predict_controller', __name__)

# function for returning the prediction based on the post data
@predict_controller.route('/', methods=['POST'])
def show():
    helper = predict_helper.PredictHelper()
    # try:
    # get model object form database by ID
    model_object = Model().find_by_id(request.form['model_id'])
    # get the actual model from the local storage by the location in the model object
    model = helper.load_model(model_object['location'])
    # except:
    #     abort(404)
    
    # get and reshape the image from the form data
    image = request.files['image']
    image = helper.reshape_image(image)

    # make a prediction and make a collection for every item in it
    raw_prediction = model.predict_classes(image)
    prediction = []
    for pred in raw_prediction:
        prediction.append(pred.item())
    
    # clear the Keras session
    helper.clear_session()

    return jsonify(prediction)