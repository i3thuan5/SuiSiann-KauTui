from behave import when, then
from phiaua.clean import clean_html
from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態


@when(u'輸入 {html}')
def 輸入(context, html):
    context.sin_html = clean_html(html)
    context.tuitse = 檢查對齊狀態


@then(u'khiām做 {kiatko}')
def khiām做(context, kiatko):
    context.test.assertEqual(str(context.sin_html), kiatko)


@when(u'有一句 {hanji} {khaugitiau}')
def 有一句(context, hanji, khaugitiau):
    sin_html = clean_html(khaugitiau)
    lomaji = sin_html.get_text()
    context.tuitse = 檢查對齊狀態(hanji, lomaji, khaugitiau)


@then(u'顯示錯誤 {tshogoo}')
def 顯示錯誤(context, tshogoo):
    context.test.assertEqual(context.tuitse, tshogoo)
