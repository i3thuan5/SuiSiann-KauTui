import json
from django.utils.html import format_html
from django.contrib import admin


class PhiauAModelAdmin(admin.ModelAdmin):
    _音檔html = '''<div><audio controls>
                <source src='{}'>
                Your browser does not support the audio element.</audio>
                </div>'''

    def 放送(self, obj):
        if obj.音檔:
            try:
                音檔網址 = obj.音檔網址
            except KeyError as e:
                return e
            return format_html(self._音檔html, 音檔網址)
        else:
            return ''

    _waveform_html = '''<div>
                <button id='hongsang'>play</button>
                <div id='waveform' data-src='{}' data-tok='{}'>wave</div>
                </div>'''

    def 海湧(self, obj):
        if obj.音檔:
            try:
                音檔網址 = obj.音檔網址
            except KeyError as e:
                return e
            return format_html(
                self._waveform_html,
                音檔網址,
                json.dumps(obj.kaldi切音時間),
            )
        else:
            return ''

    class Media:
        js = (
            'https://cdn.tiny.cloud/1/7r771z07171zzo2b460fzfdmi25680770i1u6nf3mz6uh1fs/tinymce/5/tinymce.min.js',
            'phiaua/js/lomaji.js',
            'phiaua/js/suan_lomaji.js',
            'https://unpkg.com/wavesurfer.js',
            'https://unpkg.com/wavesurfer.js/dist/plugin/wavesurfer.regions.min.js',
            'kaldi/js/waveform.js',
        )
