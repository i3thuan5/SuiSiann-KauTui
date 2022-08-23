from behave import given, when, then
# from phiaua.clean import clean_html, get_lomaji
# from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態
from SuiSiannAdminApp.models import 文章表, 句表


@given(u'有一句錄音')
def 有一句錄音(context):
    bun = 文章表.objects.create(文章名='試驗用')
    context.ku = 句表.objects.create(來源=bun)


@when(u'輸入口語調 {html}')
def 輸入(context, html):
    context.ku.羅馬字含口語調 = html
    context.ku.clean()
    context.ku.save()


@then(u'口語調khiām做 {kiatko}')
def khiām做(context, kiatko):
    context.test.assertEqual(context.ku.羅馬字含口語調, kiatko)


@when(u'漢字是 {hanji} ，口語調是 {khaugitiau}')
def 漢字_口語調(context, hanji, khaugitiau):
    context.ku.漢字 = hanji
    context.ku.羅馬字含口語調 = khaugitiau
    context.ku.clean()
    context.ku.save()


@then(u'顯示錯誤 {tshogoo}')
def 顯示錯誤(context, tshogoo):
    context.test.assertEqual(context.ku.對齊狀態, tshogoo)


@then(u'無顯示錯誤')
def 無顯示錯誤(context):
    context.test.assertEqual(context.ku.對齊狀態, '', (context.ku.漢字, context.ku.羅馬字))


@then(u'純文字羅馬字khiām做 {lomaji}')
def step_impl(context, lomaji):
    context.test.assertEqual(
        context.ku.羅馬字,
        lomaji.replace('\\n', '\n'),
    )
