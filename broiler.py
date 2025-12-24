#! /usr/bin/env python3
# or /usr/bin/python3
# or /path/to/.venv/bin/python3
# or /Users/foobar/python-venv/.venv/bin/python3

# name of the program
# what is this?
# requirements?
# syntax: program [--option] parameter


import sys, pathlib, tomllib, argparse


# ANSI SGR formatting sequences
def f(code) -> str:
    return '\x1b[' + str(code) + 'm'
def c(code) -> str:
    return f('38;5;' + str(code))

# formatted warnings
def warn(msg):
    print(c(196) + str(msg) + f(39), file=sys.stderr)

# read configuration file
def read_configuration(my_path:pathlib.Path) -> dict:
    config_path = my_path.with_suffix('.toml')
    try:
        with open(config_path, 'rb') as f:
            return tomllib.load(f)
    except Exception as e:
        warn('toml error: ' + str(e))
        return {}

# parse arguments
def get_arguments(my_name:str) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=my_name)
    parser.add_argument('parameter',
                        type=str,
                        help='parameter help')
    parser.add_argument('--option',
                        action='store_true',
                        required=False,
                        help='option help')
    return parser.parse_args()


# main program
def main() -> int:
    # my path
    my_path = pathlib.Path(__file__)
    my_dir  = str(my_path.parent)
    my_name = str(my_path.name)

    # load configuration
    config = read_configuration(my_path)

    # get arguments
    arguments = get_arguments(my_name)

    # fancy code starts here


    return 0

if __name__ == '__main__':
    sys.exit(main())
