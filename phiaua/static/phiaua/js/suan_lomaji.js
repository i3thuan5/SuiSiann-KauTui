function suan_thaubue_lomaji(suan) {
  console.log(suan.startContainer,suan.endContainer)
  suan_thautsing_lomaji(suan);
  suan_aupiah_lomaji(suan);
}

function suan_thautsing_lomaji(suan) {
  let bue_lomaji = /[^ -\.,;:?!"'\(\)“”‘’~]+$/g;
  let thaukhu = suan.startContainer, offset=suan.startOffset;
  console.log('start',suan.startContainer,suan.startOffset)
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
    console.log('thaukhu.childNodes', thaukhu.childNodes,offset,thaukhu.innerHTML)
    if(offset){
      thaukhu = thaukhu.childNodes[offset - 1];
      offset = null;
    }
    else
      thaukhu = thaukhu.lastChild;
  }
  if(!offset)
    offset = thaukhu.nodeValue.length;
  let pi = thaukhu.nodeValue.substr(0, suan.startOffset)
  let tsing = pi.match(bue_lomaji);
  console.log('tsing',tsing)
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
  let aukhu = suan.endContainer, offset=suan.endOffset;
  console.log('end',suan.endContainer,suan.endOffset,aukhu.childNodes.length)
  if(
    (aukhu.nodeType == 1 && suan.endOffset == aukhu.childNodes.length)
    || (aukhu.nodeType != 1 && suan.endOffset == aukhu.nodeValue.length)
  ) {
    if(aukhu.nextSibling) {
      aukhu = aukhu.nextSibling;
      offset = null;
    }
    else {
      aukhu = aukhu.parentNode.nextSibling;
      offset = null;
    }
  }
  if(!aukhu)
    return;
    console.log('aukhu.childNodes', aukhu,aukhu.childNodes,offset)
  while(aukhu.nodeType == 1) {
    console.log('aukhu.childNodes', aukhu.childNodes,offset)
    if(offset){
      aukhu = aukhu.childNodes[offset];
      offset = null;
    }
    else
      aukhu = aukhu.firstChild;
  }
  if(!offset)
    offset = 0;

  let aupi = aukhu.nodeValue.substr(offset);
  let au = aupi.match(thau_lomaji);
  if(au){
    suan.setEnd(
      aukhu,
      offset + au[0].length
    )
  }
}
