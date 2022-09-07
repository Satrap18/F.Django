from django import forms


class TodoCreateFrom(forms.Form):
	title = forms.CharField()
	body = forms.CharField()
	time = forms.DateTimeField()