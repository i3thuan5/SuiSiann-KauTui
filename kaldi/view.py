
from SuiSiannAdminApp.models import 句表
from django.http.response import JsonResponse


def kiamtsa(request, kuid):
    kiatko = 句表.objects.get(id=kuid).kaldi_tuìtsê()
    return JsonResponse({'LMJ': kiatko})
