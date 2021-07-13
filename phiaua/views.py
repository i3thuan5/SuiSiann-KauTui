from django.http import JsonResponse


def khuan(request, khuan_id):
    return JsonResponse({
        'iunn': 'color',
        'suan': [
              {'id': 1, 'mia': '本調', 'siktsui': 'red'},
              {'id': 2, 'mia': '規則變調', 'siktsui': 'green'},
              {'id': 3, 'mia': '仔前變調', 'siktsui': 'blue'},
              {'id': 4, 'mia': '仔前變調', 'siktsui': 'blue'},
        ]
    })
