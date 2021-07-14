from django import forms


class 句表單(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["備註"].widget = forms.widgets.Textarea(
            attrs={'rows': 2, 'cols': 100})
