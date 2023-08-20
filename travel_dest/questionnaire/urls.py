from django.urls import path

from . import views

app_name = 'questionnaire'

urlpatterns = [
    path('', views.index, name='index'),
    path('questions', views.questions, name='questions'),
    path('submit/', views.submit_form, name='submit_form'),
]