from django import forms
class textinger(forms.Form):
    text_data=forms.CharField(widget=forms.Textarea)
