import re


_html_span = re.compile('<span class="([-a-z0-9]+)">([^<>]+)</span>')
_html_p = re.compile('</?p>')


def hue_tacotron(lui, html):
    kalui = _html_span.sub(lambda ji: ji.group(2) + lui[ji.group(1)], html)
    return _html_p.sub('', kalui)
