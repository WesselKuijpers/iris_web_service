from keras.models import load_model

class PredictHelper:
    def __init__(self):
        self.model = None

    def load_model(self, model_path):
        model = load_model(model_path)
        self.model = model
        return model

    