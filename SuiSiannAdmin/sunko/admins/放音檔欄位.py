from django.utils.html import format_html
from sunko.management.算音檔網址 import 音檔網址表


class 放音檔欄位():

    def 放音檔(self, obj):
        if obj.音檔:
            try:
                音檔網址 = 音檔網址表[obj.音檔]
            except KeyError as e:
                return e
            return format_html('''<audio controls>
                <source src='{}'>
                Your browser does not support the audio element.</audio>''',
                    音檔網址
                )
        else:
            return ''
