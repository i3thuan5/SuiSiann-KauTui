function suan_thaubue_lomaji(suan) {
  console.log(suan.startContainer,suan.endContainer)
  suan_thautsing_lomaji(suan);
  suan_aupiah_lomaji(suan);
}

function suan_thautsing_lomaji(suan) {
  let bue_lomaji = /[^ -\.,;:?!"'\(\)“”‘’~]+$/g;
  let thaukhu = suan.startContainer, offset=suan.startOffset;
  if(suan.startOffset == 0) {
    if(thaukhu.previousSibling) {
      thaukhu = thaukhu.previousSibling;
      offset = null;
    }
    else {
      thaukhu = thaukhu.parentNode.previousSibling;
      offset = null;
    }
  }
  if(!thaukhu)
    return;
  while(thaukhu.nodeType == 1) {
    if(offset)
      thaukhu = thaukhu.children[offset];
    else
      thaukhu = thaukhu.lastChild;
  }
  if(!offset)
    offset = thaukhu.nodeValue.length;
  let pi = thaukhu.nodeValue.substr(0, suan.startOffset)
  let tsing = pi.match(bue_lomaji);
  if(tsing){
    suan.setStart(
      thaukhu,
      offset - (
        tsing.reverse()[0].length
      )
    )
  }
}

function suan_aupiah_lomaji(suan) {
  let thau_lomaji = /^[^ -\.,;:?!"'\(\)“”‘’~]+/g;
  let aukhu = suan.endContainer;
  while(aukhu.nodeType == 1){
    aukhu = aukhu.lastChild;
  }
  let aupi = aukhu.nodeValue
  if(suan.endOffset < aupi.length) {
    let au = (
      aupi
        .substr(suan.endOffset)
        .match(thau_lomaji)
      )
    if(au){
      suan.setEnd(
        aukhu,
        suan.endOffset + au[0].length
      )
    }
  }
  else {
    aukhu = suan.endContainer.nextSibling;
    if(!aukhu)
      aukhu = suan.endContainer.parentNode.nextSibling;
    if(aukhu){
      while(aukhu.nodeType == 1){
        aukhu = aukhu.lastChild;
      }
      console.log('suan.endContainer.parentNode',suan.endContainer.parentNode)
      let au = aukhu.nodeValue.match(thau_lomaji);
      if(au){
        let tngte = au[0].length;
        suan.setEnd(
          aukhu,
          tngte
        )
      }
    }
  }
}
