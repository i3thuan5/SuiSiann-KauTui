from django.utils.html import format_html, format_html_join


class 放音檔欄位:
    _音檔html = '''<div>{}：<audio controls>
                <source src='{}'>
                Your browser does not support the audio element.</audio></div>'''

    def 放原始全部音檔(self, obj):
        if obj.音檔:
            try:
                音檔網址 = obj.音檔網址
            except KeyError as e:
                return e
            return format_html(self._音檔html, '全部', 音檔網址)
        else:
            return ''

    def 放切好音檔(self, obj):
        return format_html_join(
            '\n',
            self._音檔html,
            enumerate(obj.kaldi切音時間網址(), start=1)
        )
