import librosa
from django.conf import settings
from kaldiliau import tuitse


threshold_db = getattr(settings, 'THRESHOLD_DB', 40.0)


def tngku(lomaji, imtong_sittse, imtong_siongtui):
    wav, sample_rate = librosa.load(
        imtong_sittse, sr=None,
    )
    librosa_kiatko = []
    for thau, bue in librosa.effects.split(
        wav, top_db=threshold_db,
        frame_length=2048, hop_length=512,
    ):
        librosa_kiatko.append(
            (thau / sample_rate, bue / sample_rate)
        )
    kaldi_kiatko = []
    for ku in tuitse(imtong_siongtui, lomaji):
        kaldi_kiatko.append(
            (ku['khaisi'], ku['kiatsok'])
        )

    return tshiâu斷句時間(
        len(wav) / sample_rate, librosa_kiatko, kaldi_kiatko
    )


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
