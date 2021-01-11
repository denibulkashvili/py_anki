"""Script Utils"""
import sys

def print_help():
    """Print help message"""
    print('Usage:')
    print('    # python generate.py [deck_name] [dir_name (optional)]')
    print('    # python generate.py my_deck my_dir')
    print('    # python generate.py my_deck home/abs/path/to/dir')

def get_args(args):
    """Parses CLI arguments  and returns deck_name and dir_name"""
    if len(args) > 1:
        deck_name = args[1]
    else:
        print("Input deck name!\n")
        print_help()
        sys.exit()

    if len(args) > 2:
        dir_name = args[2]
    else:
        dir_name = None

    return deck_name, dir_name
