from django.shortcuts import render
from django.http import HttpResponse
from . import Shedshow

# Create your views here.
def control_shed(request):
	print("control message sent")
	Shedshow.sides2()
	return HttpResponse('Control sent')