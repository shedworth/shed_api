from django import forms
from crispy_forms.helper import FormHelper

PATTERN_CHOICES = [
	(1, 'Static (colour 1)'),
	(2, 'Scan (colour 1)'),
	(5, 'Sweep (colour 1)'),
	(6, '2-colour flash (col 1 & 2)'),
	(4, '2-colour chase (col 1 & 2)'),
	(3, 'Rainbow (cols inactive)'),
]
	
class ControlForm(forms.Form):																				# Form for single fixture control
	fixture = forms.IntegerField(max_value=4, label="Fixture")	
	pattern = forms.IntegerField(max_value=255, label="Pattern")
	red_1 = forms.IntegerField(max_value=255, label="Red 1")
	green_1 = forms.IntegerField(min_value=0, max_value=255, label="Green 1")
	blue_1 = forms.IntegerField(min_value=0, max_value=255, label="Blue 1")
	red_2 = forms.IntegerField(min_value=0, max_value=255, label="Red 2")
	green_2 = forms.IntegerField(min_value=0, max_value=255, label="Green 2")
	blue_2 = forms.IntegerField(min_value=0, max_value=255, label="Blue 2")
	rate = forms.IntegerField(min_value=0, max_value=255, label="Rate")
	
class ExtendedControlForm(forms.Form):														# Form with individual field for each parameter
	#fixture = forms.IntegerField(max_value=4, label="Fixture")	
#	fixture_A = 1	
	pattern_A = forms.CharField(label="Pattern", widget=forms.Select(choices=PATTERN_CHOICES))
	red_1_A = forms.IntegerField(max_value=255, label="Red 1")
	green_1_A = forms.IntegerField(min_value=0, max_value=255, label="Green 1")
	blue_1_A = forms.IntegerField(min_value=0, max_value=255, label="Blue 1")
	red_2_A = forms.IntegerField(min_value=0, max_value=255, label="Red 2")
	green_2_A = forms.IntegerField(min_value=0, max_value=255, label="Green 2")
	blue_2_A = forms.IntegerField(min_value=0, max_value=255, label="Blue 2")
	rate_A = forms.IntegerField(min_value=0, max_value=255, label="Rate")
	#fixture_B = 2	
	pattern_B = forms.CharField(label="Pattern", widget=forms.Select(choices=PATTERN_CHOICES))
	red_1_B = forms.IntegerField(max_value=255, label="Red 1")
	green_1_B = forms.IntegerField(min_value=0, max_value=255, label="Green 1")
	blue_1_B = forms.IntegerField(min_value=0, max_value=255, label="Blue 1")
	red_2_B = forms.IntegerField(min_value=0, max_value=255, label="Red 2")
	green_2_B = forms.IntegerField(min_value=0, max_value=255, label="Green 2")
	blue_2_B = forms.IntegerField(min_value=0, max_value=255, label="Blue 2")
	rate_B = forms.IntegerField(min_value=0, max_value=255, label="Rate")
	#fixture_C = 3
	pattern_C = forms.CharField(label="Pattern", widget=forms.Select(choices=PATTERN_CHOICES))
	red_1_C = forms.IntegerField(max_value=255, label="Red 1")
	green_1_C = forms.IntegerField(min_value=0, max_value=255, label="Green 1")
	blue_1_C = forms.IntegerField(min_value=0, max_value=255, label="Blue 1")
	red_2_C = forms.IntegerField(min_value=0, max_value=255, label="Red 2")
	green_2_C = forms.IntegerField(min_value=0, max_value=255, label="Green 2")
	blue_2_C = forms.IntegerField(min_value=0, max_value=255, label="Blue 2")
	rate_C = forms.IntegerField(min_value=0, max_value=255, label="Rate")
	
class ColourPickerControlForm(forms.Form):											# Form for all fixtures with Javascript colour picker
	
	def __init__(self, *args, **kwargs):
		super(ColourPickerControlForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False
		
	pattern_A = forms.CharField(label="Pattern", widget=forms.Select(choices=PATTERN_CHOICES))
	colour_1_A = forms.CharField(widget=forms.HiddenInput())
	colour_2_A = forms.CharField(widget=forms.HiddenInput())
	rate_A = forms.IntegerField(min_value=0, max_value=255, label="Rate")
	pattern_B = forms.CharField(label="Pattern", widget=forms.Select(choices=PATTERN_CHOICES))
	colour_1_B = forms.CharField(widget=forms.HiddenInput())
	colour_2_B = forms.CharField(widget=forms.HiddenInput())
	rate_B = forms.IntegerField(min_value=0, max_value=255, label="Rate")
	pattern_C = forms.CharField(label="Pattern", widget=forms.Select(choices=PATTERN_CHOICES))
	colour_1_C = forms.CharField(widget=forms.HiddenInput())
	colour_2_C = forms.CharField(widget=forms.HiddenInput())	
	rate_C = forms.IntegerField(min_value=0, max_value=255, label="Rate")
