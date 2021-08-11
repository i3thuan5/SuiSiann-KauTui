

def tshiâu斷句時間(總時間, librosa結果, kaldi結果):
    kiatko = []
    for thau, bue in kaldi結果:
        thau, bue = float(thau), float(bue)
        khi = 0
        suah = 總時間
        for pun_thau, pun_bue in librosa結果:
            if pun_bue <= thau:
                khi = pun_bue
            if pun_thau >= bue:
                suah = pun_thau
                break
        kiatko.append(
            (khi, suah)
        )
    return kiatko
