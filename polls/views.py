from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def submit(request, question_id):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        search_results = fname + " " + lname
        question = get_object_or_404(Question, pk=question_id)
        context = { 'search_results': search_results, 'question' : question, 'question_id' : question_id }

        return render(request, 'polls/submit.html', context)
        # # Create a form instance and populate it with data from the request (binding):
        # form = submit(request.POST, question_id)

        # # Check if the form is valid:
        # if form.is_valid():
        #     search_results = fname + " " + lname
        #     question = get_object_or_404(Question, pk=question_id)
        #     context = { 'search_results': search_results, 'question' : question, 'question_id' : question_id }

        #     return render(request, 'polls/submit.html', context)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/submit.html', {'question': question})
