#!/usr/bin/env python3

from ..common.parser import set_parser
import tensorflow as tf

def load_data(data_dir, img_height=180, img_width=180, batch_size=32):
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        color_mode="rgb"
        )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        color_mode="rgb"
        )
    return train_ds, val_ds
