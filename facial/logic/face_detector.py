import numpy as np
from PIL import Image
import tensorflow as tf

from services.model_singleton import ModelSingleton


def face_detector(face):
    model = ModelSingleton.get_instance()
    img_array = np.array(face)
    return model.model.predict(tf.expand_dims(img_array, axis=0))[0]
