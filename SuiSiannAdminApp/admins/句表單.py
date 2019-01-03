from django import forms
from SuiSiannAdminApp.models import 語料狀況表


class 句表單(forms.ModelForm):
    漢字 = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 100}))
    臺羅 = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 100}))
    備註 = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 100}))

    def __init__(self, *args, **kwargs):
        super(句表單, self).__init__(*args, **kwargs)
        self.fields["語料狀況"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["語料狀況"].help_text = ""
        self.fields["語料狀況"].queryset = 語料狀況表.objects.all()
