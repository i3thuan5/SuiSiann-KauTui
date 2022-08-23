Feature: 口語調標記
    1. 標幾若字--ê，拆做一字一字
    2. 空白、連字符、輕聲符mài標


Scenario Outline: Tshiâu html
   Given 有一句錄音
    When 輸入口語調 <sujip>
    Then 口語調khiām做 <kiatko>

    Examples: 詞kah詞中央ê空白
    | sujip | kiatko |
    | <p><span class="lui-1">Hit</span> <span class="lui-2">lō</span></p> |  <p><span class="lui-1">Hit</span> <span class="lui-2">lō</span></p> |


    Examples: 詞組做伙標，ài拆開
    | sujip | kiatko |
    | <p><span class="lui-1">Hit lō</span></p> | <p><span class="lui-1">Hit</span> <span class="lui-1">lō</span></p> |


    Examples: 一个詞做伙標，ài拆開
    | sujip | kiatko |
    | <p><span class="lui-1">Hit-lō</span></p> | <p><span class="lui-1">Hit</span>-<span class="lui-1">lō</span></p> |


    Examples: 包著標點，ài提掉
    | sujip | kiatko |
    | <p><span class="lui-1">Hit-lō...</span></p> | <p><span class="lui-1">Hit</span>-<span class="lui-1">lō</span>...</p> |


    Examples: 一个字拆做兩个標仔，hōo對齊資訊處理
    | sujip | kiatko |
    | <p><span class="lui-1">Hi</span><span class="lui-2">t-lō</span></p> | <p><span class="lui-1">Hi</span><span class="lui-2">t</span>-<span class="lui-2">lō</span></p> |


    Examples: 空ê span直接提掉
    | sujip | kiatko |
    | <p><span class="lui-1">Hit</span><span class="lui-2"></span>-<span class="lui-3">lō</span></p> | <p><span class="lui-1">Hit</span>-<span class="lui-3">lō</span></p> |


    Examples: 無class ê span提掉
    | sujip | kiatko |
    | <p><span class="lui-1">tōng</span>-<span class="lui-2">sû</span><span class="lui-1">─</span><span>─</span></p> | <p><span class="lui-1">tōng</span>-<span class="lui-2">sû</span>──</p> |


    Examples: 輸入ê <p> ài完全保留
    | sujip | kiatko |
    | <p><span class="lui-1">Hit</span>-<span class="lui-3">lō</span></p><p><span class="lui-1">Guá</span>...</p> | <p><span class="lui-1">Hit</span>-<span class="lui-3">lō</span></p><p><span class="lui-1">Guá</span>...</p> |


Scenario Outline: Kiám html
   Given 有一句錄音
    When 漢字是 <hanji> ，口語調是 <lomaji>
    Then 顯示錯誤 <tshogoo>

    Examples: 一个字拆做兩个標仔，顯示標記錯誤
    | hanji | lomaji | tshogoo |
    | 彼號 | <p><span class="lui-1">Hi</span><span class="lui-2">t-l</span><span class="lui-3">ō</span></p> | Hit、lō 標記錯誤 |

    Examples: 一个字kan-na標一半，顯示標記錯誤
    | hanji | lomaji | tshogoo |
    | 彼號 | <p><span class="lui-1">Hi</span>t-l<span class="lui-3">ō</span></p> | Hit、lō 標記錯誤 |

    Examples: 規个字無標，顯示標記錯誤
    | hanji | lomaji | tshogoo |
    | 的開始。 | <p><span class="lui-8">ê</span> khai-<span class="lui-2">sí</span>.</p> | khai 標記錯誤 |

Scenario Outline: Kiám html hó-sè.
   Given 有一句錄音
    When 漢字是 <hanji> ，口語調是 <lomaji>
    Then 無顯示錯誤

    Examples: 標記正確
    | hanji | lomaji |
    | 彼號 | <p><span class="lui-1">Hit</span>-<span class="lui-3">lō</span></p> |

    Examples: 標記正確，有nbsp
    | hanji | lomaji |
    | 真重要 | <p><span class="lui-1">tsin</span> <span class="lui-1">tiōng</span>-<span class="lui-2">iàu</span></p> |

Scenario Outline: Html tsuán-tsò Tâi-bûn
   Given 有一句錄音
    When 輸入口語調 <sujip>
    Then 純文字羅馬字khiām做 <lomaji>

    Examples: 輸入ê <p> tī純文字mā ài保留
    | sujip | lomaji |
    | <p><span class="lui-1">Hit</span>-<span class="lui-3">lō</span></p><p><span class="lui-1">Guá</span>...</p> | Hit-lō\nGuá... |

    Examples: 純文字mā正常
    | sujip     | lomaji    |
    | Hit-lō... | Hit-lō... |
