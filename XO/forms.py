from django import forms

class CodeForm(forms.Form):
    gameCode = forms.CharField(label="gameCodeInput", max_length=3)