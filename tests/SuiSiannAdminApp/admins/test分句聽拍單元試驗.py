import re

from django.test import TestCase


from SuiSiannAdminApp.admins.分句聽拍欄位 import 分句欄位


class 分句聽拍單元試驗(TestCase):
    def setUp(self):
        self.textarea = re.compile('<textarea')
        self.audio = re.compile('<audio')
        self.請重切 = re.compile('請重切')

    def test_拄好三句(self):
        漢 = ['一', '二', '三', ]
        羅 = ['tsit', 'nng', 'sann', ]
        音 = ['1.wav', '2.wav', '3.wav', ]
        self.assertEqual(
            len(self.textarea.findall(str(分句欄位().分句組合(漢, 羅, 音)))),
            1 + 1
        )

    def test_拄好四句做兩區(self):
        漢 = ['一', '二', '三', '四', ]
        羅 = ['tsit', 'nng', 'sann', 'si', ]
        音 = ['1.wav', '2.wav', '3.wav', '4.wav', ]
        self.assertEqual(
            len(self.textarea.findall(str(分句欄位().分句組合(漢, 羅, 音)))),
            2 + 2
        )

    def test_音檔數量照句數(self):
        漢 = ['一', '二', '三', '四', ]
        羅 = ['tsit', 'nng', 'sann', 'si', ]
        音 = ['1.wav', '2.wav', '3.wav', '4.wav', ]
        self.assertEqual(
            len(self.audio.findall(str(分句欄位().分句組合(漢, 羅, 音)))),
            4
        )

    def test_漢羅照長的彼个(self):
        漢 = ['一', '二', '三', '四', ]
        羅 = ['tsit', ]
        音 = ['1.wav', '2.wav', '3.wav', '4.wav', ]
        self.assertEqual(
            len(self.textarea.findall(str(分句欄位().分句組合(漢, 羅, 音)))),
            2 + 2
        )

    def test_音檔較長愛顯示有加_請重切(self):
        漢 = ['一', ]
        羅 = ['tsit', ]
        音 = ['1.wav', '2.wav', '3.wav', '4.wav', ]
        kiatko = str(分句欄位().分句組合(漢, 羅, 音))
        self.assertEqual(
            len(self.audio.findall(kiatko)),
            4
        )
        self.assertEqual(
            len(self.請重切.findall(kiatko)),
            3
        )

    def test_音檔較短愛講無夠_請重切(self):
        漢 = ['一', '二', '三', '四', ]
        羅 = ['tsit', 'nng', 'sann', 'si', ]
        音 = ['1.wav', ]
        self.assertEqual(
            len(self.請重切.findall(str(分句欄位().分句組合(漢, 羅, 音)))),
            3
        )
