document.addEventListener('DOMContentLoaded', function(){
  fetch('/phiaua/khuan/1')
  .then(response => response.json())
  .then(data => {
    let lui_kiatko = data.suan;
    // lui_kiatko=[
    //   { id:1, miâ:'本調', siktsuí:'red',},
    //   { id:2, miâ:'規則變調', siktsuí:'green',},
    // ]

    let luimia = lui => lui.miâ;
    let luisik = lui => lui.siktsuí;
    let liuamia = lui => 'liua-' + lui.id;
    let tueliuamia = lui => 'tueliua-' + lui.id;
    let cssmia = lui => 'lui-' + lui.id;
    let sik = lui => 'sik-' + lui.id;
    let liuatsua = lui_kiatko.map(lui => liuamia(lui)).join(' ')
    let tueliuatsua = lui_kiatko.map(lui => tueliuamia(lui)).join(' ')
    let thautsing_html = function (node) {
      if(node){
        if(node.outerHTML) //span, p
          return thautsing_html(node.previousSibling) + node.outerHTML;
        else // text
          return thautsing_html(node.previousSibling) + node.nodeValue;
      }
      return '';
    };

    tinymce.init({
      selector: 'textarea.phiaua',

      menubar: false,  
      toolbar: 'tiongng-siann | '  + liuatsua + ' | tiongng-siann ',
      valid_elements: 'p,span[class]',
      valid_classes: lui_kiatko.map(lui => cssmia(lui)).join(' '),
      valid_styles: {'*': ''},
      setup: function (editor) {
        editor.ui.registry.addContextToolbar('textselection', {
          predicate: function (node) {
            return !editor.selection.isCollapsed();
          },
          items: 'tiongng-siann | '  + tueliuatsua + ' | tiongng-siann ',
          position: 'selection',
          scope: 'node'
        });
        editor.ui.registry.addContextToolbar('text_tshih', {
          predicate: function (node) {
            return editor.selection.isCollapsed();
          },
          items: 'tiongng-siann',
          position: 'selection',
          scope: 'node'
        });

        lui_kiatko.forEach(lui => {
          editor.ui.registry.addIcon(
            cssmia(lui),
            `<svg width="24" height="24" style="fill: ${luisik(lui)};"><path d="M17.5 11.4A9 9 0 0118 14c0 .5 0 1-.2 1.4 0 .4-.3.9-.5 1.3a6.2 6.2 0 01-3.7 3 5.7 5.7 0 01-3.2 0A5.9 5.9 0 017.6 18a6.2 6.2 0 01-1.4-2.6 6.7 6.7 0 010-2.8c0-.4.1-.9.3-1.3a13.6 13.6 0 012.3-4A20 20 0 0112 4a26.4 26.4 0 013.2 3.4 18.2 18.2 0 012.3 4zm-2 4.5c.4-.7.5-1.4.5-2a7.3 7.3 0 00-1-3.2c.2.6.2 1.2.2 1.9a4.5 4.5 0 01-1.3 3 5.3 5.3 0 01-2.3 1.5 4.9 4.9 0 01-2 .1 4.3 4.3 0 002.4.8 4 4 0 002-.6 4 4 0 001.5-1.5z" fill-rule="evenodd"></path></svg>`
          );
          let tsitma = false;
          editor.ui.registry.addToggleButton(liuamia(lui), {
            icon: cssmia(lui),
            text: luimia(lui),
            onAction: function (_) {
              const tshiau = editor.selection.isCollapsed();
              if(tshiau){
                let suan = editor.selection.getRng();
                console.log(suan, suan.startContainer.innerHTML);
                let thau_lomaji = /^[^ -\.,;:?!"'\(\)“”‘’~]+/g;
                let bue_lomaji = /[^ -\.,;:?!"'\(\)“”‘’~]+$/g;
                console.log(suan.startContainer.textContent == '\ufeff', suan.startContainer,
                suan.endContainer);
                let tsing = (
                  suan.startContainer.nodeValue
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
                let au = (
                  suan.endContainer.nodeValue
                    .substr(suan.endOffset)
                    .match(thau_lomaji)
                  )
                if(au){
                  suan.setEnd(
                    suan.endContainer,
                    suan.endOffset + au[0].length
                  )
                }
                console.log(suan);

                editor.selection.setRng(suan);
              }

              // let punte = editor.selection.getBookmark();
              editor.execCommand('RemoveFormat');
              editor.execCommand('FormatBlock', false, sik(lui));

              // editor.selection.moveToBookmark(punte);

            },
            onSetup: function (api) {
              editor.formatter.formatChanged(sik(lui), function (state) {
                api.setActive(state);
                tsitma = state;
              });
            }
          });
          editor.ui.registry.addToggleButton(tueliuamia(lui), {
            icon: cssmia(lui),
            text: luimia(lui),
            onAction: function (_) {
              editor.execCommand('RemoveFormat');
              editor.execCommand('FormatBlock', false, sik(lui));
            },
            onSetup: function (api) {
              api.setActive(tsitma);
            }
          });
        });

        editor.ui.registry.addButton('siann', {
          icon: 'arrow-right',
          text: 'Tsóng放',
          onAction: function (_) {
            let imtong = document.getElementsByTagName('audio')[0];
            imtong.pause();
            imtong.currentTime = 0;
            imtong.play();
          },
        });

        editor.ui.registry.addButton('tiongng-siann', {
          icon: 'arrow-right',
          onAction: function (_) {
            const lueiong = editor.getBody().innerHTML;
            const suan = editor.selection.getRng();
            let thautsing_longtsong = (
              thautsing_html(suan.startContainer.parentNode.previousSibling)
              + thautsing_html(suan.startContainer.previousSibling)
              + suan.startContainer.nodeValue.substr(0, suan.startOffset)
            );
            // console.log(lueiong);
            // console.log(thautsing_longtsong);
            const html_phiaua = /<.*?>/g;
            let punte = lueiong.replace(html_phiaua, '').length;
            let phiaukau = thautsing_longtsong.replace(html_phiaua, '').length;
            let imtong = document.getElementsByTagName('audio')[0];
            let bio = phiaukau/punte*imtong.duration - 2;
            if(bio < 0)
              bio = 0;
            // console.log(bio, phiaukau, punte);
            imtong.pause();
            imtong.currentTime = bio;
            imtong.play();
          },
        });
      },

      content_style: lui_kiatko.map(lui => (
        `
          .${cssmia(lui)} \{ ${data.iunn}: ${luisik(lui)}; \}
          .${cssmia(lui)}::selection \{ color: white; background-color: ${luisik(lui)}; \}
        `
      )).join(' ') + 'p::selection { color: white; background-color: black; }',
      // content_style: 
      //   '.lui-1 { color: green; } ' +
      //   '.lui-2 { color: red; } ',

      formats: Object.fromEntries(
        lui_kiatko.map(lui => [
          sik(lui), {classes: cssmia(lui), inline: 'span', exact: true}
        ])
      ),
      // formats: {
      //   'sik-1': { inline: 'span', classes: 'lui-1', exact: true },
      //   'sik-2': { inline: 'span', classes: 'lui-2', exact: true },
      // },

      style_formats: lui_kiatko.map(lui => (
        { title: luimia(lui), format: sik(lui) }
      )),
      // style_formats: [
      //   { title: '本調', format: 'sik-1' },
      //   { title: '變調', format: 'sik-2' },
      // ],
    });


  });
});