from flask import Flask, Blueprint
import deploy
from controllers.file_controller import file_controller
from controllers.model_controller import model_controller
from controllers.predict_controller import predict_controller

# app entry point

# call the deploy script
deployer = deploy.Deployer()
# check if the database is up-to-date
# if not, forward the required schema's
# if it is, continue
deployer.forward_schema()


# required variable for registering blueprints
app = Flask(__name__)

# controller classes
# TODO: make dynamic controller imports and register_blueprint
# app.register_blueprint(file_controller, url_prefix="/file")
app.register_blueprint(model_controller, url_prefix="/model")
app.register_blueprint(predict_controller, url_prefix="/predict")