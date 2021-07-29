from django.utils.html import format_html, format_html_join


class 放音檔欄位:
    _音檔html = '''<div><audio controls>
                <source src='{}'>
                Your browser does not support the audio element.</audio></div>'''

    def 放送(self, obj):
        if obj.音檔:
            try:
                音檔網址 = obj.音檔網址
            except KeyError as e:
                return e
            return format_html(self._音檔html, 音檔網址)
        else:
            return ''
