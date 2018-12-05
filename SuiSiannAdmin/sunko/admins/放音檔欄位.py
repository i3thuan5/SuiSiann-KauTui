from django.utils.html import format_html
from sunko.management.記音檔所在 import 音檔所在表
from os.path import isfile
from urllib.parse import urlencode


class 放音檔欄位():

    def 放音檔(self, obj):
        if obj.音檔:
            try:
                音檔完整所在 = 音檔所在表[obj.音檔]
            except KeyError as e:
                return e
            return format_html('''<audio controls>
                <source src='{}'>
                Your browser does not support the audio element.</audio>''',
                    音檔完整所在
                )
        else:
            return ''
