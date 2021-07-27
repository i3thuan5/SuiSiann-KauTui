function suan_thaubue_lomaji(editor) {
  let suan = editor.selection.getRng();
  let thau_lomaji = /^[^ -\.,;:?!"'\(\)“”‘’~]+/g;
  let bue_lomaji = /[^ -\.,;:?!"'\(\)“”‘’~]+$/g;
  console.log(suan.startContainer,suan.endContainer)
  let pi;
  if(suan.startContainer.nodeType == 1) {
    pi = suan.startContainer.innerText;
  }
  else {
    pi = suan.startContainer.nodeValue;
  }
  let tsing = (
    pi
    .substr(0, suan.startOffset)
    .match(bue_lomaji)
  );
  if(tsing){
    suan.setStart(
      suan.startContainer,
      suan.startOffset - (
        tsing.reverse()[0].length
      )
    )
  }
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
  return suan;
}