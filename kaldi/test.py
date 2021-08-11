from django.test.testcases import TestCase
from kaldi.lib.換算切音所在 import 換算切音所在


class 換算切音所在單元試驗(TestCase):
    def tearDown(self):
        執行 = 換算切音所在(self.總時間, self.librosa結果, self.kaldi結果)
        self.assertEqual(len(執行), len(self.預期))
        for 一執行, 一預期 in zip(執行, self.預期):
            for 一所在, 一數字 in zip(一執行, 一預期):
                self.assertAlmostEqual(
                    一所在, 一數字
                )

    def test_一句_還完整一句(self):
        self.總時間 = 2.503
        self.librosa結果 = [
            [0.35, 0.90], [0.95, 1.15],
        ]
        self.kaldi結果 = [
            [
                "0.6900000000000001",  # head
                "1.14",  # end
            ],
        ]
        self.預期 = [[0.0, 2.503, ], ]

    def test_兩句_邊仔恬盡量濟(self):
        self.總時間 = 2.503
        self.librosa結果 = [
            [0.35, 0.90], [0.95, 1.15],
            [1.22, 1.73], [1.95, 2.15],
        ]
        self.kaldi結果 = [
            ["0.69", "1.14"],
            ["1.23", "2.04"],
        ]
        self.預期 = [
            [0.0, 1.22, ],
            [1.15, 2.503, ],
        ]
