from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from . import Shedshow
from .forms import ControlForm
# Create your views here.
def control_shed(request):
	submitted = False
	if request.method == 'GET':
		form = ControlForm(initial={	'pattern': 1,
																			'red_1': 0,
																			'green_1': 0,
																			'blue_1': 0,
																			'red_2': 0,
																			'green_2': 0,
																			'blue_2': 0,
																			'rate': 50,
																		})
		if 'submitted' in request.GET:
			submitted = True
	
	if request.method == 'POST':
		form = ControlForm(request.POST)
		if form.is_valid():
			shed_params = {
				'fixture': 0,		
				'pattern': 1, 
				'red_1': 0,
				'blue_1': 0,
				'green_1': 0,
				'red_2': 0,
				'green_2': 0,
				'blue_2': 0,
				'rate': 0,
			}
		
			for parameter in request.POST:
				if parameter in shed_params.keys():
					shed_params[parameter] = int(request.POST.get(parameter))
		
			print(shed_params)
			Shedshow.control_shed(shed_params)
	
	return render(request, 'home.html', {'form': form, 'submitted': submitted})	
	
		#return HttpResponse('Control sent')
	



