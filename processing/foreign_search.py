import re
from processing.tokenization import tokenize


def foreign_search(s: str) -> str:
    s = tokenize(s)
    indices = []
    for i, token in enumerate(x for x in re.split(r'[ ;:\n+*/=!?"\']', s) if x not in ' ;:\n+*/=!?"\'.,'):
        if re.search(r'[A-z]+-?[A-z]*', token) is not None:
            indices.append(str(i))
    return ', '.join(indices)
