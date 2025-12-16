from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from .models import Question


def index(request):
    #Pega as primeiras 5 perguntas mais recentes
    latest_question_list = Question.objects.order_by("-pub_date") [:5]
    template = loader.get_template("polls/index.html")
    #Junta as perguntas em uma string só
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})