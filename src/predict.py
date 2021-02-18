#!/usr/bin/env python3

import tensorflow as tf
import numpy as np
# from .common.parser import set_parser
from common.parser import set_parser
import os
import sys


def get_classes(path_to_sample_dir):
    """
    Assuming each class is a subdir in `path_to_sample_dir`
    """
    all_subdirs = [x[1] for x in os.walk(path_to_sample_dir)]
    classes = all_subdirs[0]
    return classes

def make_decision(score, class_names,lower_bound=None):
    if lower_bound is None:
        # -- sets default to a random choise
        lower_bound = 1./len(class_names)
    if np.asarray(score).all() <= lower_bound:
        print("El algoritmo no puede afirmar que la imagen pertenezca a ninguna\
                clase conocida, segun la cota provista.")
    else:
        print("Esta imagen probablemente pertenece a {} con un porcentaje de confianza de {:.2f}".format(class_names[np.argmax(score)], 100*np.max(score)))
    return

def main(argv):
    # -- Get path to images and model.
    # parser = config_Parse()
    args = set_parser()
    # args = parser.get_args()
    path_model = args.model_path
    path_img_to_predict = args.input_img
    img_height = int(args.img_height)
    img_width = int(args.img_width)

    class_names = get_classes(args.samples_path)

    # -- Load model
    clf = tf.keras.models.load_model(filepath=path_model)

    # -- Load image
    img = tf.keras.preprocessing.image.load_img(
            path_img_to_predict,
            target_size=(img_height, img_width)
            )
    img_arr = tf.keras.preprocessing.image.img_to_array(img)
    img_arr = tf.expand_dims(img_arr, 0)

    # -- Predict
    prediction = clf.predict(img_arr)
    score = tf.nn.softmax(prediction[0])
    make_decision(score, class_names)

    return

if __name__ == '__main__':
    main(sys.argv[1:])
