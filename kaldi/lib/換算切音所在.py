

def 換算切音所在(總時間, kaldi結果):
    if len(kaldi結果) == 1:
        return [[0.0, 總時間]]
    結果 = []
    for 一段 in kaldi結果:
        pass