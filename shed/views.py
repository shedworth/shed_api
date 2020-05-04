from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from . import Shedshow
from .forms import ControlForm
# Create your views here.
def control_shed(request):
	submitted = False
	if request.method == 'GET':
		initial_values = Shedshow.stored_values
		initial_values['fixture'] = 0
		initial_values['pattern'] = 1
		form = ControlForm(initial=initial_values)
		if 'submitted' in request.GET:
			submitted = True
	
	if request.method == 'POST':
		form = ControlForm(request.POST)
		if form.is_valid():
			shed_params = Shedshow.stored_values
		
			for parameter in request.POST:
				if parameter in shed_params.keys():
					shed_params[parameter] = int(request.POST.get(parameter))
		
			print(shed_params)
			Shedshow.control_shed(shed_params)
	
	return render(request, 'home.html', {'form': form, 'submitted': submitted})	
	
		#return HttpResponse('Control sent')
	



