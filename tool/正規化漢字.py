import re


括號 = re.compile('（.*）|\(.*\)')

def 漢字正規化(hanji):
    kiatKo = 括號.sub('', hanji)
    return kiatKo 