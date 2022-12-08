from django import forms


class SubmitCodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'id': 'code', 'class': 'form-control'}))

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'id': 'comment', 'class': 'form-control'}))

