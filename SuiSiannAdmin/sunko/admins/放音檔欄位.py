from django.utils.html import format_html


class 放音檔欄位():

    def 放音檔(self, obj):
        if obj.音檔:
            return format_html('''<audio controls>
            <source src='/wavs/{}'>
            Your browser does not support the audio element.</audio>''',
                obj.音檔
            )
        else:
            return ''
