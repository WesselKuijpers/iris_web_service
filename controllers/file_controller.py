from flask import Flask, Blueprint

file_controller = Blueprint('file_controller', __name__)

# function for accessing files
# TODO: rethink routing / file controller in general (plugging?)
@file_controller.route('/<folder>/<file>')
def show(self, folder, file):
    #TODO: should return a file from the filesystem instead of a string
    file = "reach for the sky, mister"
    return file