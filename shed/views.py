from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from . import Shedshow
from .forms import ControlForm, ExtendedControlForm
import copy
# Create your views here.
def control_shed(request):
	submitted = False
	if request.method == 'GET':
		initial_values = copy.deepcopy(Shedshow.stored_values_A)
		initial_values.update(Shedshow.stored_values_B)
		initial_values.update(Shedshow.stored_values_C)
		initial_values['fixture'] = 0
		initial_values['pattern'] = 1
		form = ExtendedControlForm(initial=initial_values)
		if 'submitted' in request.GET:
			submitted = True
	
	if request.method == 'POST':
		form = ExtendedControlForm(request.POST)
		if form.is_valid():
			
			shed_params_A = {}
			for parameter in request.POST:
				#print(request.POST.get(parameter))
				if parameter in Shedshow.stored_values_A.keys():	
					Shedshow.stored_values_A[parameter] = request.POST.get(parameter)	
					shed_params_A[str(parameter[:-2])] = int(request.POST.get(parameter))	
			shed_params_A['fixture'] = 1
			Shedshow.control_shed(shed_params_A)
			
			shed_params_B = {}
			for parameter in request.POST:
				if parameter in Shedshow.stored_values_B.keys():
					Shedshow.stored_values_B[parameter] = request.POST.get(parameter)	
					shed_params_B[str(parameter[:-2])] = int(request.POST.get(parameter))				
			shed_params_B['fixture'] = 2
			Shedshow.control_shed(shed_params_B)
			
			shed_params_C = {}
			for parameter in request.POST:
				if parameter in Shedshow.stored_values_C.keys():
					Shedshow.stored_values_C[parameter] = request.POST.get(parameter)						
					shed_params_C[str(parameter[:-2])] = int(request.POST.get(parameter))	
			shed_params_C['fixture'] = 3
			Shedshow.control_shed(shed_params_C)
		
	return render(request, 'home.html', {'form': form, 'submitted': submitted})	
	
		#return HttpResponse('Control sent')
	



