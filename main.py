import argparse
from pathlib import Path
from os import mkdir
from number_interchange import interchange

parser = argparse.ArgumentParser(description='Replace numbers in the text with their written form.')
parser.add_argument('directory', type=str, metavar='D', help='A directory with text files to change')


if __name__ == '__main__':
    args = parser.parse_args()
    dir_name = args.directory

    p = Path(dir_name)
    files = [x for x in p.iterdir() if x.is_file()]

    p_res = p / 'res'
    mkdir(p_res)

    for file in files:
        with file.open() as f:
            s = f.read()
            s_new = interchange(s)

            with open(p_res / file.name, 'x+') as f_res:
                f_res.write(s_new)
