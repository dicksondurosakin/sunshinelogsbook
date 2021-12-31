from django.urls import path
from . import views

app_name = 'logsbook'

urlpatterns = [
    path('',views.logs, name='logs')
]