from SuiSiannAdminApp.models import 句表


def 提原始漢羅kah漢羅():
    原始漢羅 = []
    漢羅 = []
    
    全部句 = 句表.objects.all()
    for 一句 in 全部句:
        原始漢羅.extend([str(一句.pk), 一句.原始漢字, 一句.原始臺羅])
        漢羅.extend([str(一句.pk), 一句.漢字, 一句.臺羅])
    
    return (原始漢羅, 漢羅)