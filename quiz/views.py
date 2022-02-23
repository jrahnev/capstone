from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.db.models import Max
import random
import json

# Create your views here.

def index(request):
    return render(request, "quiz/index.html")

def start(request):
    return render (request, "quiz/test.html")

def display(request):
    max_number = Question.objects.aggregate(Max('level'))['level__max']
    questions = Question.objects.filter(level=1,number=random.randint(1,max_number))
    request.session["answer"] = questions[0].answer
    request.session['level'] = 1
    request.session["attempts"] = 1
    request.session['question_ides'] = [questions.last().id]
    request.session['counter'] = 0
    return JsonResponse([question.serialize() for question in questions], safe=False)

def newquestion(request,answer):
    max_number = Question.objects.aggregate(Max('level'))['level__max']
    if request.session['attempts'] == max_number:
        return HttpResponseRedirect(reverse('end'))
    level = request.session['level']
    if answer == request.session['answer']:
        questions = random.choice(Question.objects.filter(level=level + 1))
        request.session['answer'] = questions.answer
        request.session['level'] += 1
        request.session["attempts"] += 1
        request.session['counter'] += 1
        return JsonResponse([questions.serialize()], safe=False)
    else:
        if len(request.session['question_ides']) > 0:
            questions = Question.objects.all()
            for num in request.session["question_ides"]:
                questions = questions.exclude(id=num)
        questions = random.choice(questions.filter(level=level))
        request.session['answer'] = questions.answer
        request.session["attempts"] += 1
        request.session["question_ides"].append(questions.id)
    return JsonResponse([questions.serialize()], safe=False)

def end(request):
    level = ''
    max_number = Question.objects.aggregate(Max('level'))['level__max']
    if request.session['attempts'] == max_number:
        if request.session["counter"] == 0:
            level = "Basic level"
        elif request.session["counter"] < max_number/4:
            level = 'Beginner'
        elif request.session["counter"] < 2*(max_number/4):
            level = 'Preintermediate'
        elif request.session["counter"] < 3*(max_number/4):
            level = 'Intermediate'
        elif request.session["counter"] <= max_number:
            level = 'Advanced'
        return render (request,'quiz/end.html',{
        'level':level
        })
    else:
        return render(request,'quiz/end.html')