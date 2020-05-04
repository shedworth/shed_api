from django.shortcuts import render
from django.http import HttpResponse
from . import Shedshow

# Create your views here.
def control_shed(request):
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
	
	for parameter in request.GET:
		if parameter in shed_params.keys():
			shed_params[parameter] = int(request.GET.get(parameter))
	
	print(shed_params)
	Shedshow.shedMove(shed_params)
















#	colour_switcher = { 
#		'purple': Shedshow.sides1, 
#		'yellow': Shedshow.sides2, 
#		'red': Shedshow.sides3,
#		'green': Shedshow.sides4,
#		'blue': Shedshow.sides5,
#		'off': Shedshow.sidesblack,
#	 }
#			
#	colour = request.GET.get('colour', '')
#	colour_func = colour_switcher.get(colour, lambda: "Invalid choice")
#	colour_func()
#	
#	chase = request.GET.get('chase', '')
	
	
	print("control message sent")
	return HttpResponse('Control sent')