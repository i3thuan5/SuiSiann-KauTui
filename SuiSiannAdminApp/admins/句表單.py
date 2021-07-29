from django import forms


class 句表單(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["漢字"].widget = forms.widgets.Textarea(
            attrs={'rows': 3, 'cols': '100'})
        self.fields["羅馬字含口語調"].widget = forms.widgets.Textarea(
            attrs={'class': 'phiaua'})
        self.fields["備註"].widget = forms.widgets.Textarea(
            attrs={'rows': 2, 'cols': 100})
