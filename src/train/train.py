#!/usr/bin/env python3

import tensorflow as tf
import sys
from ..common.parser import set_parser
from ..preprocess.load_data import load_data
from ..model.models import build_MultiClassCNN_ex

def main(argv):
    parser = set_parser()
    args = parser.parse_args()
    data_dir = args.samples_path
    epochs = int(args.num_epochs)
    metrics_list = args.metrics
    callbacks_list = args.callbacks


    train_ds, val_ds = load_data(data_dir=data_dir) # init others params as default

    # -- Get all classes
    classes = train_ds.class_names
    num_classes = len(classes)

    # -- Load in performance mode
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1e3).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    # -- Set model
    # clf = MultiClassCNN(
            # input_shape=(img_height,img_width,3),
            # ).build()
    clf = MultiClassCNN_ex(
            input_shape=(img_height, img_width, 3),
            num_classes=num_classes
            )

    # FIXME metrics_list and callbacks_list not really implemented
    clf.compile(
            optimizer = "adam",
            loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics = metrics_list
            )
    # -- Train on data
    clf.fit(
            train_ds,
            validation_data=val_ds,
            epochs=epochs,
            callbacks=callbacks_list
            )


    # -- Save results

    return


if __name__ == '__main__':
    main(sys.argv[1:])
