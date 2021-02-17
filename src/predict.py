#!/usr/bin/env python3

import argparse
def config_Parse():
    """
    Set all the configuration to your parser object.

    # Args::None

    # Returns::parser object.
    """
    parser = argparse.ArgumentParser('name')
    parser.add_argument('-I', '--Input', required=True, help='<Input folder or file/s>' )
    parser.add_argument('-O', '--Output', required=True, help='<Output folder or files/s>')
    parser.add_argument('-D','--Debug', required=False, help='Debug flag', action='store_true')
    parser.add_argument('-M','--MaxEvents', required=False, help='Set maximum of events. Default -1 == all', type=int, default=-1)
    return parser

# -- Get path to images and model.

# -- Load model

# -- Predict
