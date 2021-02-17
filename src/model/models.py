#!/usr/bin/env python3
#=============#
# Author: Santiago Noacco Rosende
# Contact: snoaccor@cern.ch
# GitLab:https://gitlab.cern.ch/snoaccor
# GitHub:https://github.com/santinoacco
#=============#

import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras import layers
from tensorflow.keras import initializers
from tensorflow.keras.optimizers import Adam

class Base_CNN(object):
    def __init__(
            self, input_shape,
            max_nConvKernels, max_nConvLayers,
            max_nDenseKernels, max_nDenseLayers,
            ):
        assert isinstance(input_shape, tuple),\
                "'input_shape' must be a tuple"
        self.input_shape = input_shape
        assert isinstance(max_nConvLayers, int),\
                "'max_nConvLayers' must be int"
        self.nCL = max_nConvLayers
        assert isinstance(max_nConvKernels, int),\
                "'max_nConvKernels' must be int"
        self.nCK = max_nConvKernels
        assert isinstance(max_nDenseLayers, int),\
                "'max_nDenseLayers' must be int"
        self.nDL = max_nDenseLayers
        assert isinstance(max_nDenseKernels,int),\
                "'max_nDenseKernels must be int"
        self.nDK = max_nDenseKernels

class MultiClassCNN(Base_CNN):
    def __init__(
            self, input_shape,
            max_nConvKernels, max_nConvLayers, max_nConvBlocks,
            max_nDenseKernels, max_nDenseLayers, max_nDenseBlocks,
            dropout_rate, ConvAct, num_classes
            ):
        super().__init__(input_shape, max_nConvKernels, max_nConvLayers, max_nDenseKernels, max_nDenseLayers)
        assert isinstance(max_nConvBlocks,int),\
                "'max_nConvBlocks must be int"
        self.nCB = max_nConvBlocks
        assert isinstance(max_nDenseBlocks,int),\
                "'max_nDenseBlocks must be int"
        self.nDB = max_nDenseBlocks
        self.dr = dropout_rate
        self.ConvAct=ConvAct
        self.k_init = initializers.VarianceScaling(
                scale=2.0,
                mode='fan_in',
                distribution='uniform'
                )
        self.num_classes = num_classes
        # -- Build Model
        self.build()

    def build(self):
        self.model = Sequential()
        self.model.add(
                    Conv2D(
                        self.nCK,
                        kernel_size=2,
                        activation=self.ConvAct,
                        input_shape=self.input_shape
                        )
                    )
        for lyr in range(self.nCL-1):
            self.model.add(
                        Conv2D(
                            self.nCK,
                            kernel_size=2,
                            activation=self.ConvAct,
                            )
                        )
        self.model.add(MaxPooling2D((2, 2)))
        # == 2nd Conv Block ==
        self.model.add(
                Conv2D(
                    32,
                    kernel_size=2,
                    activation=self.ConvAct,
                    )
                )
        self.model.add(Flatten())

        # NOTE: is a Block of M layers and 1 Dropout
        # -- Dense 1st block
        for lyr in range(self.nDL):
            self.model.add(
                        Dense(
                            self.nDK,
                            activation='relu',
                            kernel_initializer=self.k_init,
                            bias_initializer='zeros'
                            )
                        )
        self.model.add(Dropout(self.dr));
        # -- Dense 2nd block
        self.model.add(
                    Dense(
                        64,
                        activation='relu',
                        kernel_initializer=self.k_init,
                        bias_initializer='zeros'
                        )
                    )

        # -- Output probabilities
        self.model.add(
                Dense(
                    self.num_classes,
                    activation='sigmoid',
                    kernel_initializer=self.k_init,
                    bias_initializer='zeros'
                    )
                )


def build_MultiClassCNN_ex(input_shape,num_classes):
    model = Sequential()
    model.add(layers.experimental.preprocessing.Rescaling(1./255, input_shape=input_shape)),
    model.add(layers.Conv2D(16, 3, padding='same', activation='relu'))
    model.add(layers.MaxPooling2D())
    model.add(layers.Conv2D(32, 3, padding='same', activation='relu'))
    model.add(layers.MaxPooling2D())
    model.add(layers.Conv2D(64, 3, padding='same', activation='relu'))
    model.add(layers.MaxPooling2D())
    model.add(layers.Dropout(0.2))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(num_classes))

    return model
