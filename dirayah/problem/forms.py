from django import forms


class SubmitCodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 100, 'id': 'code'}))

