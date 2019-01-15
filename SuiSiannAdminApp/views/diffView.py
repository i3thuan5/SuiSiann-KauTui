from django.http import HttpResponse
from django.views import View
from SuiSiannAdminApp.management.提原始漢羅kah漢羅 import 提原始漢羅kah漢羅
import diff_match_patch

class DiffView(View):

    def get(self, request, *args, **kwargs):
        全部句 = 提原始漢羅kah漢羅()
#         全部句 = [] 
        全部比對html = self.顯示比對(全部句)
        return HttpResponse(全部比對html)
    
    def 顯示比對(self, 全部句):
        dmp = diff_match_patch.diff_match_patch()
        全部比對html = ''
        for 原始句, 句 in zip(全部句[0], 全部句[1]):
            if 原始句 == 句:
                比對html = '<p>{}</p>'.format(原始句)
            else:
                diff = dmp.diff_main(原始句, 句)
                dmp.diff_cleanupEfficiency(diff)
                # 拆兩組
                紅色 = []
                青色 = []
                for 一組 in diff:
                    if 一組[0] == -1:
                        紅色.append(一組)
                    elif 一組[0] == 1:
                        青色.append(一組)
                    else:
                        # = 0
                        紅色.append(一組)
                        青色.append(一組)
                delHtml = dmp.diff_prettyHtml(紅色)
                insHtml = dmp.diff_prettyHtml(青色)
                比對html = (('<p><span style="background:#ffeef0">{}</span>'+
                '<br/><span style="background:#e6ffed">{}</span></p>').format(delHtml, insHtml)
                )
            全部比對html += 比對html  
            
        return 全部比對html
