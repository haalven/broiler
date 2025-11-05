#! /usr/bin/env python3
# or /usr/bin/python3
# or /path/to/.venv/bin/python3
# or /Users/foobar/python-venv/.venv/bin/python3

# name of the program
# what is this?
# requirements?
# syntax: program [--option] parameter


import sys, pathlib, tomllib, argparse

DEBUG_LEVEL = 1


# ANSI SGR formatting sequences
def f(code): return '\x1B[' + str(code) + 'm'
def c(code): return f('38;5;' + str(code))

# warnings
def warn(msg:str):
    global DEBUG_LEVEL
    if DEBUG_LEVEL:
        print(c(196) + str(msg) + f(39),
              file=sys.stderr)

# read TOML file
def read_configuration(my_path:Path) -> dict:
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

def main() -> int:
    # my path
    my_path = pathlib.Path(__file__)
    my_dir  = str(my_path.parent)
    my_name = str(my_path.name)

    # load configuration file
    config = read_configuration(my_path)

    # get arguments.parameter and arguments.option
    arguments = get_arguments(my_name)

    # fancy code starts here


    return 0

if __name__ == '__main__':
    sys.exit(main())
