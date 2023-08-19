from django.shortcuts import render

from .models import Question, Choice
# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questionnaire/index.html', context)

def question1(request, question_id):
    context = {'question': Question.objects.get(pk=question_id)}
    return render(request, 'questionnaire/question1.html', context)

def question2(request, question_id):
    context = {'question': Question.objects.get(pk=question_id)}
    return render(request, 'questionnaire/question2.html', context)

def submit_form(request, curr_q, question_id):
    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')  # 'choice' is the name of the input field
        # Now you have the ID of the selected choice
        # You can process it as needed, e.g., retrieve the choice from the database
        selected_choice = Choice.objects.get(id=selected_choice_id)
        print("Selected choice:", selected_choice.choice)
    context = {'question': Question.objects.get(pk=question_id)}
    return render(request, 'questionnare/question' + str(curr_q) + '.html', context)