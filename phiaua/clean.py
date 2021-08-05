from kesi.butkian.kongiong import si_lomaji
from bs4 import BeautifulSoup


def clean_html(羅馬字含口語調):
    ku_html = BeautifulSoup(羅馬字含口語調, 'html.parser')
    sin_html = BeautifulSoup('<p></p>', 'html.parser')
    # 猶未標口語調ê純文字
    if not ku_html.p:
        return ku_html

    for phiau_tag in ku_html.p.contents:
        # 這个content是純文字
        if phiau_tag.name is None:
            sin_html.p.append(str(phiau_tag))
        else:
            lui = phiau_tag['class']
            sin_tag = None
            for jiguan in phiau_tag.string:
                if si_lomaji(jiguan):
                    if sin_tag is None:
                        sin_tag = sin_html.new_tag('span', attrs={'class': lui})
                        sin_tag.string = ''
                    sin_tag.string += jiguan
                else:
                    if sin_tag is not None:
                        sin_html.p.append(sin_tag)
                        sin_tag = None
                    sin_html.p.append(jiguan)
            if sin_tag is not None:
                sin_html.p.append(sin_tag)

    return sin_html
