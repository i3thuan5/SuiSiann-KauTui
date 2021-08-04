from behave import given, then
from phiaua.hue import hue_tacotron


@given('口語調類型')
def 口語調類型(context):
    context.lui = {}
    for tsua in context.table:
        context.lui['lui-{}'.format(tsua['id'])] = tsua['代']


@then('口語調 {html} ê 格式是 {tacotron}')
def tacotron格式(context, html, tacotron):
    context.test.assertEqual(
        hue_tacotron(context.lui, html),
        tacotron
    )
