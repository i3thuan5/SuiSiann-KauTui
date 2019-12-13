from django.test.testcases import TestCase
from kaldi.lib.換算切音所在 import 換算切音所在


class 換算切音所在單元試驗(TestCase):
    def tearDown(self):
        執行 = 換算切音所在(self.總時間, self.kaldi結果)
        self.assertEqual(len(執行), len(self.預期))
        for 一執行, 一預期 in zip(執行, self.預期):
            for 一所在, 一數字 in zip(一執行, 一預期):
                self.assertAlmostEqual(
                    一所在, 一數字
                )

    def test_一句_還完整一句(self):
        self.總時間 = 2.503
        self.kaldi結果 = [
            [
                "0.6900000000000001",  # head
                "1.14",  # end
             ],
        ]
        self.預期 = [[0.0, 2.503, ], ]

    def test_兩句_還兩句切佇中央(self):
        self.總時間 = 2.503
        self.kaldi結果 = [
            [
                "0.6900000000000001",
                "1.14",
            ],
            [
                "1.23",
                "2.04",
            ]
        ]
        self.預期 = [[0.0, 1.185, ], [1.185, 2.503, ], ]

    def test_四句_還四句(self):
        self.總時間 = 9.027
        self.kaldi結果 = [
            [
                "0.66",
                "1.65",
            ],
            [
                "1.83",
                "3.63",
            ],
            [
                "3.93",
                "6.57",
            ],
            [
                "6.93",
                "8.43",
            ]
        ]
        self.預期 = [[0.0, 1.74, ], [1.74, 3.78, ],
                   [3.78, 6.75, ], [6.75, 9.027, ], ]

    def test_兩句1到2_2到3_還兩句(self):
        self.總時間 = 4
        self.kaldi結果 = [
            [
                "1",
                "2.6",
            ],
            [
                "3",
                "3.6",
            ]
        ]
        self.預期 = [[0.0, 2.8, ], [2.8, 4.0, ], ]
