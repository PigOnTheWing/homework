import re


def check(s: str) -> str:
    match = re.search(r'\d[а-яa-z]|[а-яa-z]\d|[.,:;!?"\'][а-яa-z]|[а-яa-z][.,:;!?"\']', s, re.IGNORECASE)
    while match is not None:
        s = s[:match.start(0) + 1] + ' ' + s[match.start(0) + 1:]
        match = re.search(r'\d[а-яa-z]|[а-яa-z]\d|[.,:;!?"\'][а-яa-z]|[а-яa-z][.,:;!?"\']', s, re.IGNORECASE)
    return s


def tokenize(s: str) -> str:
    tokens = [check(t) for t in s.split(' ') if t != '']
    return ' '.join(tokens)
