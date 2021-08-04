Feature: Huē做tacotron
    匯做tacotron較利便ê格式。


Scenario Outline: 媠聲規範
    Given 口語調類型
      | id  | 代  |
      | 1   | 規  |
      | 2   | 本  |
      | 3   | 再  |
      | 4   | 固  |
      | 5   | 隨  |
      | 6   | 仔  |
      | 7   | 三  |
      | 8   | 海  |

    Then  口語調 <html> ê 格式是 <tacotron>

    Examples: 有標點句。
      | html                                                                                                                                                                                                                                                                                                          | tacotron                                                                  |
      | <p><span class="lui-1">Hit</span> <span class="lui-2">lō</span>...</p>                                                                                                                                                                                                                                        | Hit規-lō本...                                                             |
      | <p><span class="lui-1">Sa̋i-ióo-ná</span>-<span class="lui-2">lah</span>, <span class="lui-2">goodbye</span>! <span class="lui-7">Bîn</span>-<span class="lui-1">á</span>-<span class="lui-2">tsài</span> <span class="lui-1">tsiah</span> <span class="lui-1">koh</span> <span class="lui-2">lâi</span>.</p> | Sa̋i規-ióo規-ná規-lah本, goodbye本! Bîn仔-á規-tsài本 tsiah規 koh再 lâi本. |

