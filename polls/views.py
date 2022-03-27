from django.shortcuts import render, get_object_or_404, redirect

from .models import Question
from .models import Group

from .forms import *

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

# Cheryl
def image_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/polls/group/' + str(form.cleaned_data.get('group').id))
    else:
        form = PersonForm()
        
    return render(request, 'polls/images.html', {'form': form})

#Dylan
import sqlite3
def groups(request):
    if request.method == 'POST':
        if request.POST.get('fname') != None:
            name_input = request.POST.get('fname')
            #check if group already exists
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            sqlcommand1 = 'SELECT group_name FROM polls_group WHERE group_name = \'' + str(name_input) + '\''
            cursor.execute(sqlcommand1)
            if len(cursor.fetchall()) != 0:
                group_list = Group.objects.order_by('-group_name')
                msg = 'Group Already Exists'
                error = 1
                context = {
                    'group_list': group_list,
                    'error_msg': msg,
                    'error':error
                }
                return render(request, 'polls/homepage.html', context)
            #create group in SQL
            group = Group(group_name = name_input)
            group.save()

            sqlcommand2 = 'SELECT id FROM polls_group WHERE id = ' + str(group.id)
            cursor.execute(sqlcommand2)
            reslist = cursor.fetchall()
            result = str(reslist[0])
        else:
            group_id = request.POST.get('gname')
            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            sqlcommand = 'SELECT id FROM polls_group WHERE group_name = \'' + str(group_id) + '\'' 
            cursor.execute(sqlcommand)
            reslist = cursor.fetchall()
            if len(reslist) == 0:
                group_list = Group.objects.order_by('-group_name')
                msg = 'Group Doesn\'t Exists'
                error = 2
                context = {
                    'group_list': group_list,
                    'error_msg': msg,
                    'error':error
                }
                return render(request, 'polls/homepage.html', context)
            result = str(reslist[0])
        return redirect('group/' + result[1:len(result)-2])

    group_list = Group.objects.order_by('-group_name')
    context = {
        'group_list': group_list,
        'error_msg':'',
        'error':0
    }
    return render(request, 'polls/homepage.html', context)

def group_detail(request, group_id):

    group = get_object_or_404(Group, pk=group_id)

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    sqlcommand = 'SELECT * FROM polls_person WHERE group_id = ' + str(group_id)
    cursor.execute(sqlcommand)
    reslist = cursor.fetchall()
    peoples_cups = { }
    peoples_duration = { }
    peoples_distance = { }
    for data in reslist:
        if data[1] in peoples_cups.keys():
            peoples_cups[data[1]] += data[5]
            peoples_duration[data[1]] += data[3]
            peoples_distance[data[1]] += data[4] 
        else:
            peoples_cups[data[1]] = data[5]
            peoples_duration[data[1]] = data[3]
            peoples_distance[data[1]] = data[4] 
    
    group.update_days_left()
    peoples_duration = sorted(peoples_duration.items(), key=lambda x: x[1], reverse=True)
    peoples_distance = sorted(peoples_distance.items(), key=lambda x: x[1], reverse=True)
    peoples_cups = sorted(peoples_cups.items(), key=lambda x: x[1], reverse=True)
    print(peoples_cups)
    return render(request, 'polls/detail.html', {"peoples_duration" : peoples_duration, "peoples_distance" : peoples_distance, "peoples_cups" : peoples_cups, "group" : group, "group_id": group_id})


def submit(request, group_id):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        search_results = fname + " " + lname
        group = get_object_or_404(Group, pk=group_id)
        context = { 'search_results': search_results, 'group' : group, 'group_id' : group_id }

        return render(request, 'polls/submit.html', context)

    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'polls/submit.html', {'group': group})

def image_gallery(request, group_id):
    
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    sqlcommand = 'SELECT image FROM polls_person WHERE group_id = ' + str(group_id) + ' AND image != \'0\'' 
    cursor.execute(sqlcommand)
    reslist = cursor.fetchall()
    img_list = []
    for x in reslist:
        tmp = str(x)
        img_list.append(tmp[1:len(tmp)-2])

    group = get_object_or_404(Group, pk=group_id)
    context = {
        'group': group,
        'group_id': group_id,
        'image_list':img_list
    }
    return render(request, 'polls/image_gallery.html', context)
