

def 換算切音所在(總時間, kaldi結果):
    # N = 1
    kaldi結果數 = len(kaldi結果)
    if kaldi結果數 == 1:
        return [[0.0, 總時間]]
    # N >= 2
    換算結果 = []
    頂一中央 = 0.0
    for ind in range(1, kaldi結果數):
        # [head0, duration0], [head1, duration1], ...
        頂句尾 = float(kaldi結果[ind - 1][1])
        句頭 = float(kaldi結果[ind][0])
        中央 = (句頭 + 頂句尾) / 2
        換算結果.append([頂一中央, 中央, ])
        頂一中央 = 中央
    # 補上尾一組
    換算結果.append([頂一中央, 總時間, ])
    return 換算結果
