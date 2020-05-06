from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import control_shed, ControlShedAjaxView

urlpatterns = [
	path('ajax/', ControlShedAjaxView.as_view(), name='control_shed_ajax'),
	path('success/', TemplateView.as_view(template_name="success.html"), name='success'),	
	url('', control_shed, name='control_shed'),
	]