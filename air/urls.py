from django.urls import include, path

from air.forms import CustomAuthenticationForm
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('sensors/', views.sensor_list, name='sensor_list'),
    path('sensors/<int:sensor_id>/', views.sensor_detail, name='sensor_detail'),
    path('sensors/add/', views.add_sensor, name='add_sensor'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
