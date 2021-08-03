Feature: 口語調標記
    1. 標幾若字--ê，拆做一字一字
    2. 空白、連字符、輕聲符mài標


Scenario: 詞kah詞中央ê空白
    When 輸入 <p><span class="lui-1">Hit</span> <span class="lui-2">lō</span></p>
    Then khiām做 <p><span class="lui-1">Hit</span> <span class="lui-2">lō</span></p>


Scenario: 詞組做伙標，ài拆開
    When 輸入 <p><span class="lui-1">Hit lō</span></p>
    Then khiām做 <p><span class="lui-1">Hit</span> <span class="lui-1">lō</span></p>


Scenario: 一个詞做伙標，ài拆開
    When 輸入 <p><span class="lui-1">Hit-lō</span></p>
    Then khiām做 <p><span class="lui-1">Hit</span>-<span class="lui-1">lō</span></p>


Scenario: 包著標點，ài提掉
    When 輸入 <p><span class="lui-1">Hit-lō...</span></p>
    Then khiām做 <p><span class="lui-1">Hit</span>-<span class="lui-1">lō</span>...</p>
