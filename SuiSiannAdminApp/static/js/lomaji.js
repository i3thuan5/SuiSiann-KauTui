
tinymce.init({
  selector: 'textarea.lomaji',

  menubar: false,  
  toolbar: 'undo redo | styleselect | punliua pianliua',
  setup: function (editor) {

    editor.ui.registry.addToggleButton('punliua', {
      text: '本調',
      onAction: function (_) {
        
        editor.execCommand('RemoveFormat');
        editor.execCommand('FormatBlock', false, 'pun');
      },
      onSetup: function (api) {
        editor.formatter.formatChanged('pun', function (state) {
          api.setActive(state);
        });
      }
    });
    editor.ui.registry.addToggleButton('pianliua', {
      text: '規則變調',
      onAction: function (_) {
        
        editor.execCommand('RemoveFormat');
        editor.execCommand('mceToggleFormat', false, 'pian');
      },
      onSetup: function (api) {
        editor.formatter.formatChanged('pian', function (state) {
          api.setActive(state);
        });
      }
    });
    
    editor.ui.registry.addContextToolbar('textselection', {
      predicate: function (node) {
        return !editor.selection.isCollapsed();
      },
      items: 'punliua pianliua',
      position: 'selection',
      scope: 'node'
    });
  },
  plugins: 'table wordcount',
  content_style: 
    '.pun_class { color: green; } ' +
    '.pian_class { color: red; } ',
  formats: {
    pun: { inline: 'span', classes: 'pun_class' },
    pian: { inline: 'span', classes: 'pian_class' },
  },
  style_formats: [
    { title: '本調', format: 'pun' },
    { title: '變調', format: 'pian' },
  ]
});

