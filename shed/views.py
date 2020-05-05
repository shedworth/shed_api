from django.shortcuts import render
from . import Shedshow
from .forms import ExtendedControlForm
import copy
# Create your views here.
def control_shed(request):
	submitted = False
	
	if request.method == 'GET':
		initial_values = {**Shedshow.stored_values_A, **Shedshow.stored_values_B, **Shedshow.stored_values_C}				# Set form values to currently held values
		form = ExtendedControlForm(initial=initial_values)																																					# Form to send to template, initialised with currently held values
		if 'submitted' in request.GET:
			submitted = True
	
	if request.method == 'POST':
		form = ExtendedControlForm(request.POST)
		if form.is_valid():
			
			for fixture, stored_values in Shedshow.fixture_list.items():												# Iterate through the three fixtures
				shed_params = {}																																		# Create empty dictionary
				for parameter in request.POST:																										# Iterate through parameters received from form
					if parameter in stored_values.keys():																						# If parameter relates to this fixture:
						stored_values[parameter] = request.POST.get(parameter)										# Update stored value in memory
						shed_params[str(parameter[:-2])] = int(request.POST.get(parameter))			# Add parameter to shed_params dictionary
				shed_params['fixture'] = fixture																										# Add fixture number to shed_params dictionary
				Shedshow.control_shed(shed_params)																						# Send shed_params to shed
						
	return render(request, 'home.html', {'form': form, 'submitted': submitted})	
	
	



