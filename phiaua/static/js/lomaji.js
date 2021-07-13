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
    let cssmia = lui => 'lui-' + lui.id;
    let sik = lui => 'sik-' + lui.id;
    let liuatsua = lui_kiatko.map(lui => liuamia(lui)).join(' ')

    tinymce.init({
      selector: 'textarea.phiaua',

      menubar: false,  
      toolbar: 'undo redo | styleselect | '  + liuatsua,
      valid_classes: lui_kiatko.map(lui => cssmia(lui)).join(' '),
      valid_styles: {'*': ''},
      setup: function (editor) {
        editor.ui.registry.addContextToolbar('textselection', {
          predicate: function (node) {
            return !editor.selection.isCollapsed();
          },
          items: liuatsua,
          position: 'selection',
          scope: 'node'
        });

        lui_kiatko.forEach(lui =>
          editor.ui.registry.addToggleButton(liuamia(lui), {
            text: luimia(lui),
            onAction: function (_) {
              
              editor.execCommand('RemoveFormat');
              editor.execCommand('FormatBlock', false, sik(lui));
            },
            onSetup: function (api) {
              editor.formatter.formatChanged(sik(lui), function (state) {
                api.setActive(state);
              });
            }
          })
        )
      },

      content_style: lui_kiatko.map(lui => `.${cssmia(lui)} \{ ${data.iunn}: ${luisik(lui)}; \}`).join(' '),
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