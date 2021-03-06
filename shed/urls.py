from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import control_shed, ControlShedAjaxView, fire_shed, run_preset

urlpatterns = [
	#path('ajax/', ControlShedAjaxView.as_view(), name='control_shed_ajax'),
	path('success/', TemplateView.as_view(template_name="success.html"), name='success'),	
	path('fire/', fire_shed, name='fire_shed'),	
	path('preset/', run_preset, name='run_preset'),	
	path('', ControlShedAjaxView.as_view(), name='control_shed_ajax'),
	]