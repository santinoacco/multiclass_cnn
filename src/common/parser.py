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

    # not implemented yet
    global_parser.add(
            '--loglevel',
            required=False,
            # default='warning',
            help="Log level (info/debug/warning)")

    global_parser.add('-gO',
            '--g_outdir',
            env_var='GLOBAL_OUTDIR',
            required=True,
            help='Output directory for the whole package')

    global_parser.add('-S',
            '--samples_path',
            required=False,
            help='path to dir containing classes subdirs')

    # ==== PERFORMANCE TRAINNING==== #
    global_parser.add(
            '--use_img_augmentation',
            action='store_true',
            required=False,
            help="Option to use Image Augmentation Generators",
            )

    # ==== SAVING/LOADING MODEL ==== #
    global_parser.add('-Swgt',
            '--save_wgts_only',
            action='store_true',
            required=False,
            help="(bool), wheather to save only model weights and architecture (True),\
                    or (False) to save everything using SavedModel TF format.\
                    Carefull support for TF_v1 is not ensured!"
            )

    global_parser.add('-Parch',
            '--path_2arch',
            required=False,
            default=None,
            help='(path)'
            )

    global_parser.add('-Pwgt',
            '--path_2weights',
            required=False,
            default=None,
            help='(path)'
            )

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

