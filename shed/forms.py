from django import forms

class ControlForm(forms.Form):
	fixture = forms.IntegerField(max_value=4, label="Fixture")	
	pattern = forms.IntegerField(max_value=255, label="Pattern")
	red_1 = forms.IntegerField(max_value=255, label="Red 1")
	green_1 = forms.IntegerField(min_value=0, max_value=255, label="Green 1")
	blue_1 = forms.IntegerField(min_value=0, max_value=255, label="Blue 1")
	red_2 = forms.IntegerField(min_value=0, max_value=255, label="Red 2")
	green_2 = forms.IntegerField(min_value=0, max_value=255, label="Green 2")
	blue_2 = forms.IntegerField(min_value=0, max_value=255, label="Blue 2")
	rate = forms.IntegerField(min_value=0, max_value=255, label="Rate")