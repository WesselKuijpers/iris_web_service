from keras.models import load_model
import tensorflow as tf
import skimage.io as io
import os
from keras import backend as k

class PredictHelper:
    def __init__(self):
        self.model = None

    def load_model(self, model_path):
        model = load_model(model_path)
        self.model = model
        return model

    def reshape_image(self, image):
        image_name = image.name
        image.save('temp/' + image_name)
        image = io.imread('temp/' + image_name, as_gray=True)
        image = image.reshape(-1, 28, 28, 1)
        os.remove('temp/' + image_name)
        return image

    def clear_session(self):
        if k.clear_session():
            return True
        else:
            return False