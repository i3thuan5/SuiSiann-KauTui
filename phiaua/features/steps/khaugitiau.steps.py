from behave import when, then
from phiaua.clean import clean_html


@when(u'輸入 {html}')
def 輸入(context, html):
    context.sin_html = clean_html(html)


@then(u'khiām做 {kiatko}')
def khiām做(context, kiatko):
    context.test.assertEqual(str(context.sin_html), kiatko)
