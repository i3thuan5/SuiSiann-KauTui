import re

# 處理全形括號kah半形括號
括號 = re.compile('[（(].*?[）)]')


def 提掉漢字的括號(hanji):
    kiatKo = 括號.sub('', hanji)
    return kiatKo
