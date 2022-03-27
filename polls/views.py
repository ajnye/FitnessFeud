from django.shortcuts import render, get_object_or_404, redirect

from .models import Question
from .models import Group

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

import sqlite3

def groups(request):
    print(request.method)
    if request.method == 'POST':
        if request.POST.get('fname') != None:
            name_input = request.POST.get('fname')
            #create group in SQL
            group = Group(group_name = name_input)
            group.save()

            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            sqlcommand = 'SELECT id FROM polls_group WHERE id = ' + str(group.id)
            cursor.execute(sqlcommand)
            reslist = cursor.fetchall()
            result = str(reslist[0])
        else:
            group_id = request.POST.get('gname')
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            sqlcommand = 'SELECT id FROM polls_group WHERE group_name = \'' + str(group_id) + '\'' 
            print(sqlcommand)
            cursor.execute(sqlcommand)
            reslist = cursor.fetchall()
            result = str(reslist[0])
            print(result)
        return redirect('group/' + result[1:len(result)-2])

    group_list = Group.objects.order_by('-group_name')
    context = {
        'group_list': group_list
    }
    return render(request, 'polls/homepage.html', context)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_group_list = Group.objects.order_by('?')
    context = {
        'latest_question_list': latest_question_list, 'latest_group_list' : latest_group_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # peoples = get_object_or_404(Group, pk=group_id).person_set.all().order_by('name')[:3]
    return render(request, 'polls/detail.html', {"question" : question})

def group_detail(request, group_id):
    # question = get_object_or_404(Question, pk=question_id)
    # peoples = get_object_or_404(Group, pk=group_id).person_set.order_by('name')[:3]
    peoples = get_object_or_404(Group, pk=group_id)
    print(peoples)
    return render(request, 'polls/detail.html', {"peoples" : peoples})

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