from django.shortcuts import render

from .models import Question, Choice
# Create your views here.

def index(request):
    return render(request, 'questionnaire/index.html')

def questions(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questionnaire/questions.html', context)

def submit_form(request):
    ids = {}
    if request.method == 'POST':

        questions = Question.objects.all()
        
        for question in questions:
            question_id = question.id
            selected_choice_id = request.POST.get('choice{}'.format(question_id))
            ids[question_id] = selected_choice_id
            
    return render(request, 'questionnaire/destination.html', {'ids': ids})

