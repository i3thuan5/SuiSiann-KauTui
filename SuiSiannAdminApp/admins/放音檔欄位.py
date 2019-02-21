from django.utils.html import format_html, format_html_join
from SuiSiannAdminApp.management.算音檔網址 import 音檔網址表


class 放音檔欄位():
    _音檔html = '''<audio controls>
                <source src='{}'>
                Your browser does not support the audio element.</audio>'''

    def 放音檔(self, obj):
        if obj.音檔:
            try:
                音檔網址 = 音檔網址表[obj.音檔]
            except KeyError as e:
                return e
            return format_html(self._音檔html, 音檔網址)
        else:
            return ''

    def 放切好音檔(self, obj):
        return format_html_join('\n', self._音檔html,    obj.kaldi切音時間)
