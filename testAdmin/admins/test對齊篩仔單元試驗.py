from django.test import TestCase
from django.contrib.admin.sites import site
from SuiSiannAdminApp.models import 句表
from SuiSiannAdminApp.admins.句後台 import 句後台
from SuiSiannAdminApp.management.檢查對齊狀態 import 檢查對齊狀態
from django.test.client import RequestFactory
from django.contrib.auth.models import User


class 對齊篩仔單元試驗(TestCase):
    request_factory = RequestFactory()
    alfred = User.objects.create_superuser('alfred', 'alfred@example.com', 'password')
    
    def test_一筆無對齊(self):
        原始漢字 = "媠"
        原始臺羅 = ""
        句表.objects.create(
            原始漢字=原始漢字,
            原始臺羅=原始臺羅,
            漢字=原始漢字,
            臺羅=原始臺羅,
            對齊狀態=檢查對齊狀態(原始漢字, 原始臺羅)
        )
        原始漢字 = "媠"
        原始臺羅 = "suí"
        句表.objects.create(
            原始漢字=原始漢字,
            原始臺羅=原始臺羅,
            漢字=原始漢字,
            臺羅=原始臺羅,
            對齊狀態=檢查對齊狀態(原始漢字, 原始臺羅)
        )
        
        modeladmin = 句後台(句表, site)
        request = self.request_factory.get('/', {
            'tuitse': '2'},
        )
        request.user = self.alfred
        changelist = modeladmin.get_changelist_instance(request)
        
        # Make sure the correct queryset is returned
        queryset = changelist.get_queryset(request)
        self.assertEqual(list(queryset), [])