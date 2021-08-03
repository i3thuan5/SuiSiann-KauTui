from SuiSiannAdminApp.models.句表 import clean_html
from behave import when, then


@when(u'輸入 {html}')
def 輸入(context, html):
    context.sin_html = clean_html(html)


@then(u'khiām做 {kiatko}')
def khiām做(context, kiatko):
    context.test.assertEqual(str(context.sin_html), kiatko)

