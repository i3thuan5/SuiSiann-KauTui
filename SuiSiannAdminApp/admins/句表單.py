from django import forms


class 句表單(forms.ModelForm):
    漢字 = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 100}))
    臺羅 = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 100}))
