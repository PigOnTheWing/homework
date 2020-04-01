import argparse
from pathlib import Path
from os import mkdir
from processing.number_interchange import interchange
from processing.tokenization import tokenize
from processing.number_search import search
from processing.foreign_search import foreign_search

parser = argparse.ArgumentParser(description='Process text files in a specific way',
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('directory', type=str, metavar='D', help='A directory with text files to change')
parser.add_argument('-m', '--mode', type=int, metavar='M',
                    choices=[1, 2, 3, 5], required=True,
                    help='Specify operation: '
                         '\n\t1 for tokenization, '
                         '\n\t2 for number search, '
                         '\n\t3 for foreign words search, '
                         '\n\t4 for replacing numbers with their written form')

ops = {1: tokenize,
       2: search,
       3: foreign_search,
       4: interchange
       }


if __name__ == '__main__':
    args = parser.parse_args()
    dir_name = args.directory
    op = ops[args.mode]

    p = Path(dir_name)
    files = [x for x in p.iterdir() if x.is_file()]

    p_res = p / 'res'
    mkdir(p_res)

    for file in files:
        with file.open() as f:
            s = f.read()
            s_new = op(s)

            with open(p_res / file.name, 'x+') as f_res:
                f_res.write(s_new)
