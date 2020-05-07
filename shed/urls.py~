from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import control_shed, ControlShedAjaxView, fire_shed

urlpatterns = [
	#path('ajax/', ControlShedAjaxView.as_view(), name='control_shed_ajax'),
	path('success/', TemplateView.as_view(template_name="success.html"), name='success'),	
	path('fire/', fire_shed, name='fire_shed'),	
	path('', ControlShedAjaxView.as_view(), name='control_shed_ajax'),
	]