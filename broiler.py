#!/usr/bin/env python3
# or #!/usr/bin/python3
# or #!/path/to/.venv/bin/python3

# name of the program
# what is this?
# requirements?
# syntax: program [--option] parameter


import sys, os.path, tomllib, argparse


# read TOML file
def read_configuration(my_dir, my_name):
    config_file = os.path.splitext(my_name)[0] + '.toml'
    config_path = os.path.join(my_dir, config_file)
    try:
        with open(config_path, 'rb') as f:
            return tomllib.load(f)
    except: return None

# parse arguments
def get_arguments(my_name):
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
    my_path = os.path.abspath(__file__)
    my_dir  = os.path.dirname(my_path)
    my_name = os.path.basename(my_path)

    # load configuration file
    config = read_configuration(my_dir, my_name)

    # get arguments.parameter and arguments.option
    arguments = get_arguments(my_name)

    # fancy code starts here

    return 0

if __name__ == '__main__':
    sys.exit(main())
