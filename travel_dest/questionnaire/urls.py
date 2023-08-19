from django.urls import path

from . import views

app_name = 'questionnaire'

urlpatterns = [
    path('', views.index, name='index'),
    path('question1<int:question_id>', views.question1, name='question1'),
    path('submit_form/', views.submit_form, name='submit_form'),
]