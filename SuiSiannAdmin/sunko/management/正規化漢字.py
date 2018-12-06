import re


括號 = re.compile('（.*）|\(.*\)')

def 提掉漢字的括號(hanji):
    kiatKo = 括號.sub('', hanji)
    return kiatKo 