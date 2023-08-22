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
    
    results = ['varadero', 'zermatt', 'kyoto', 'prague', 'newyork', 'rome']
    result = ''

    for qid in ids:
        cid = ids[qid]
        qnum = Question.objects.get(pk=qid).questionNumber
        cnum = Choice.objects.get(pk=cid).optionNumber

        if qnum == 1 and cnum == 1: # ([prague] newyork [rome]) ([veradero] [zermatt] kyoto)
            # likes resorts
            print('resorts')
            if ('prague') in results: results.remove('prague')
            if ('newyork') in results: results.remove('newyork')
            if ('rome') in results: results.remove('rome')
        elif qnum == 1 and cnum == 2:
            # prefers sight seeing
            if ('varadero') in results: results.remove('varadero')
            if ('zermatt') in results: results.remove('zermatt')
            if ('kyoto') in results: results.remove('kyoto')
        elif qnum == 2 and cnum == 1:
            # sunny
            if ('prague') in results: results.remove('prague')
            if ('zermatt') in results: results.remove('zermatt')
        elif qnum == 2 and cnum == 2:
            # not sunny
            if ('varadero') in results: results.remove('varadero')
            if ('rome') in results: results.remove('rome')
        elif qnum == 3 and cnum <= 2:
            if 'newyork' in results and 'prague' in results:
                result = 'prague'
            elif 'newyork' in results:
                result = 'newyork'
            elif 'kyoto' in results and 'varadero' in results:
                result = 'varadero'
            else: 
                result = 'manali'
        elif qnum == 3 and cnum == 3:
            if 'zermatt' in results:
                result = 'zermatt'
            else:
                result = 'kyoto'
        elif qnum == 3 and cnum == 4:
            if 'newyork' in results:
                result = 'rome'
            else: 
                result = 'kyoto'

    return render(request, 'questionnaire/destination.html', {'dest': result.upper()})

