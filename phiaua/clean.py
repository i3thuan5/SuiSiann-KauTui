from kesi.butkian.kongiong import si_lomaji
from bs4 import BeautifulSoup


def clean_html(khaugi_html):
    parser = BeautifulSoup(khaugi_html, 'html.parser')
    p = parser.find('p')
    sin_html = BeautifulSoup('<p></p>', 'html.parser')
    for i, phiau in enumerate(p.contents):
        phiau_tag = phiau.extract()
        # 這个content是純文字
        if phiau_tag.name is None:
            sin_html.p.append(phiau_tag)
        else:
            lui = phiau_tag['class']
            tag = None
            for jiguan in phiau_tag.string:
                if si_lomaji(jiguan):
                    if tag is None:
                        tag = sin_html.new_tag('span', attrs={'class': lui})
                        tag.string = ''
                    tag.string += jiguan
                else:
                    if tag is not None:
                        sin_html.p.append(tag.extract())
                        tag = None
                    sin_html.p.append(jiguan)
            if tag is not None:
                sin_html.p.append(tag.extract())

    return sin_html
