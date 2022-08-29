from kesi.butkian.kongiong import si_lomaji
from bs4 import BeautifulSoup
from phiaua.models import Luī


def clean_html(羅馬字含口語調):
    ku_html = BeautifulSoup(羅馬字含口語調, 'html.parser')
    sin_html = BeautifulSoup('', 'html.parser')
    # 猶未標口語調ê純文字
    if not ku_html.p:
        return 羅馬字含口語調

    for ku_html_p in ku_html.find_all('p'):
        sin_html_p = sin_html.new_tag('p')
        for phiau_tag in ku_html_p.contents:
            if phiau_tag.string is None:
                continue

            # 這个content是純文字
            if phiau_tag.name is None:
                sin_html_p.append(str(phiau_tag))
            else:
                try:
                    lui = phiau_tag['class']
                except KeyError:
                    sin_html_p.append(phiau_tag.string)
                    continue
                sin_tag = None
                for jiguan in phiau_tag.string:
                    if si_lomaji(jiguan):
                        if sin_tag is None:
                            sin_tag = sin_html.new_tag('span', attrs={'class': lui})
                            sin_tag.string = ''
                        sin_tag.string += jiguan
                    else:
                        if sin_tag is not None:
                            sin_html_p.append(sin_tag)
                            sin_tag = None
                        sin_html_p.append(jiguan)
                if sin_tag is not None:
                    sin_html_p.append(sin_tag)
        sin_html.append(sin_html_p)

    return str(sin_html)


def piann_haikhau_piantiau(羅馬字含口語調):
    html = BeautifulSoup(羅馬字含口語調, 'html.parser')
    # 猶未標口語調ê純文字
    if not html.p:
        return 羅馬字含口語調
    海口腔變調 = Luī.objects.get(miâ='海口腔變調（5=>3）')
    規則變調 = Luī.objects.get(miâ='規則變調')
    for p in html.find_all('p'):
        for span in p.find_all('span', class_=f'lui-{海口腔變調.id}'):
            span['class'] = f'lui-{規則變調.id}'
    return str(html)


def get_lomaji(羅馬字含口語調):
    html = BeautifulSoup(羅馬字含口語調, 'html.parser')
    if not html.p:
        return 羅馬字含口語調

    tshue = html.find_all('p')

    if tshue:
        return '\n'.join(map(lambda x: x.get_text(), tshue))
    return html.get_text()
