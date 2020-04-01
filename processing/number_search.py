import re
from processing.tokenization import tokenize


def search(s: str) -> str:
    s = tokenize(s)
    indices = []
    for i, token in enumerate(x for x in re.split(r'[ ;:\-\n+*/=!?"\']', s) if x != ''):
        if re.search(r'\d+[.,]?\d*', token) is not None:
            indices.append(str(i))
    return ', '.join(indices)
