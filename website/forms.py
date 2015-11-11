from django import forms

class SubscribeForm(forms.Form):
	name = forms.CharField()
	e-mail = forms.EmailField(required-True)
	type = forms.CharField()