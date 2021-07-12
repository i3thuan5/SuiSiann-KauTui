from django.test import TestCase
from django.contrib.admin.sites import site
from SuiSiannAdminApp.models import 句表
from SuiSiannAdminApp.admins.句後台 import 句後台
from django.test.client import RequestFactory
from django.contrib.auth.models import User


class 對齊篩仔單元試驗(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
        self.alfred = User.objects.create_superuser(
            'alfred', 'alfred@example.com', 'password')

    def tearDown(self):
        modeladmin = 句後台(句表, site)
        request = self.request_factory.get('/', {
            'tuitse': self.網址},
        )
        request.user = self.alfred
        changelist = modeladmin.get_changelist_instance(request)

        # Make sure the correct queryset is returned
        queryset = changelist.get_queryset(request)
        self.assertEqual(list(queryset), self.結果)

    def test_一筆無對齊(self):
        self.網址 = "2"
        句一 = self.新增句表("媠", "")
        self.新增句表("媠", "suí")
        self.結果 = [句一]

    def test_一筆對齊(self):
        self.網址 = "1"
        self.新增句表("媠", "")
        句二 = self.新增句表("媠", "suí")
        self.結果 = [句二]

    def 新增句表(self, 漢字, 臺羅):
        句 = 句表.objects.create(
            原始漢字=漢字,
            原始羅馬字=臺羅,
            漢字=漢字,
            羅馬字含口語調=臺羅
        )
        句.full_clean()
        句.save()
        return 句
