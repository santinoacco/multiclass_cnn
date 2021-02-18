#!/usr/bin/env python3
"""
File: Parser
Author: Noacco Santiago
Email:
Github:
Description: Parser object to use across the package
"""
import configargparse
import yaml

def set_parser():
    parser_ini = configargparse.ArgParser(
            config_file_parser_class=configargparse.ConfigparserConfigFileParser
            )
    global_parser = parser_ini
    # -- Set arguments for command line
    global_parser.add('-c',
            '--config',
            is_config_file=True,
            required=True)

    global_parser.add('-V',
            '--verbose',
            required=False,
            default=1,
            help="verbosity level, default 1 == true.\
                    If true, prints std output on screen.")

    global_parser.add('-gO',
            '--g_outdir',
            env_var='GLOBAL_OUTDIR',
            required=True,
            help='Output directory for the whole package')

    global_parser.add('-S',
            '--samples_path',
            required=False,
            help='path to dir containing classes subdirs')

    global_parser.add('-M',
            '--model_path',
            required=False,
            help='path to model')

    global_parser.add('-I',
            '--input_img',
            required=True,
            help='path to img')

    global_parser.add(
            '--img_height',
            required=False,
            help='Height of the target image size, in pixels.')

    global_parser.add(
            '--img_width',
            required=False,
            help='Width of the target image size, in pixels.')

    # ==== PERFORMANCE TRAINNING==== #
    global_parser.add(
            '--use_img_augmentation',
            action='store_true',
            required=False,
            help="Option to use Image Augmentation Generators",
            )

    # ==== SAVING/LOADING MODEL ==== #
    global_parser.add('-nEp',
            '--num_epochs',
            help="",)

    global_parser.add('-lr',
            '--learning_rate',
            help="")

    global_parser.add('-bt',
            '--batch_size',
            required=False,
            type=int,
            default=128,
            help="")

    global_parser.add_argument('--arch',
            type=yaml.safe_load,
            required=False,
            default=None,
            help="dictionary to set model architecture config."
            )

    global_parser.add_argument('--metrics',
            type=yaml.safe_load,
            required=False,
            default=None,
            help="metrics list to implement"
            )

    global_parser.add_argument('--callbacks',
            type=yaml.safe_load,
            required=False,
            default=None,
            help="callbacks dictionary")

    return global_parser.parse_args()

# def set_ini_parser(config_file):
    # cfg = configparser.ConfigParser()
    # cfg.read(config_file)
    # return cfg
    # ==== OPTIONAL EXTRA I/O ==== #
    # global_parser.add('--dp_in',
            # required=False,
            # default=None,
            # help='Input directory for DataProcessing/')

    # global_parser.add('--dp_out',
            # required=False,
            # default=None,
            # help='Output directory for DataProcessing/')

    # global_parser.add('--train_in',
            # required=False,
            # default=None,
            # help='Input directory for NeuralNetworks/Train/')

    # global_parser.add('--train_out',
            # required=False,
            # default=None,
            # help='Output directory for NeuralNetworks/Train/')

    # global_parser.add('--val_in',
            # required=False,
            # default=None,
            # help='Input directory for NeuralNetworks/Train/')

    # global_parser.add('--val_out',
            # required=False,
            # default=None,
            # help='Output directory for NeuralNetworks/Train/')
    #=========================== #

