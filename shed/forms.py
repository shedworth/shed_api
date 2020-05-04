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
	
class ExtendedControlForm(forms.Form):
	#fixture = forms.IntegerField(max_value=4, label="Fixture")	
	fixture_A = 1	
	pattern_A = forms.IntegerField(max_value=255, label="Pattern")
	red_1_A = forms.IntegerField(max_value=255, label="Red 1")
	green_1_A = forms.IntegerField(min_value=0, max_value=255, label="Green 1")
	blue_1_A = forms.IntegerField(min_value=0, max_value=255, label="Blue 1")
	red_2_A = forms.IntegerField(min_value=0, max_value=255, label="Red 2")
	green_2_A = forms.IntegerField(min_value=0, max_value=255, label="Green 2")
	blue_2_A = forms.IntegerField(min_value=0, max_value=255, label="Blue 2")
	rate_A = forms.IntegerField(min_value=0, max_value=255, label="Rate")
	fixture_B = 2	
	pattern_B = forms.IntegerField(max_value=255, label="Pattern")
	red_1_B = forms.IntegerField(max_value=255, label="Red 1")
	green_1_B = forms.IntegerField(min_value=0, max_value=255, label="Green 1")
	blue_1_B = forms.IntegerField(min_value=0, max_value=255, label="Blue 1")
	red_2_B = forms.IntegerField(min_value=0, max_value=255, label="Red 2")
	green_2_B = forms.IntegerField(min_value=0, max_value=255, label="Green 2")
	blue_2_B = forms.IntegerField(min_value=0, max_value=255, label="Blue 2")
	rate_B = forms.IntegerField(min_value=0, max_value=255, label="Rate")
	fixture_C = 3
	pattern_C = forms.IntegerField(max_value=255, label="Pattern")
	red_1_C = forms.IntegerField(max_value=255, label="Red 1")
	green_1_C = forms.IntegerField(min_value=0, max_value=255, label="Green 1")
	blue_1_C = forms.IntegerField(min_value=0, max_value=255, label="Blue 1")
	red_2_C = forms.IntegerField(min_value=0, max_value=255, label="Red 2")
	green_2_C = forms.IntegerField(min_value=0, max_value=255, label="Green 2")
	blue_2_C = forms.IntegerField(min_value=0, max_value=255, label="Blue 2")
	rate_C = forms.IntegerField(min_value=0, max_value=255, label="Rate")