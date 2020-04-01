import re


singles = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
tens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырынадцать',
        'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'
        ]
doubles = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']


def interchange(s: str) -> str:
    doubles_indices = [(x.start(0), x.end(0)) for x in re.finditer(r'\D\d{2}\D', s)]

    for i in doubles_indices[::-1]:
        num = s[i[0] + 1: i[1] - 1]

        if num[0] == '1':
            replacement = '{0}'.format(tens[int(num[1])])
        else:
            replacement = '{0} {1}'.format(doubles[int(num[0])], singles[int(num[1])])

        s = s[: i[0] + 1] + replacement + s[i[1] - 1:]

    singles_indices = [x.start(0) + 1 for x in re.finditer(r'\D\d\D', s)]

    for i in singles_indices:
        num = s[int(i)]

        replacement = 'ноль' if num == '0' else '{0}'.format(singles[int(num)])

        s = s[:i] + replacement + s[i + 1:]

    return s
