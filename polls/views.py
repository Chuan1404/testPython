from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    questions = Question.objects.all()
    options = {
        "questions": questions
    }

    return render(request, template_name="index.html", context=options)


def detail(request, id):
    options = {
        "id": id
    }
    return render(request, template_name="question_detail.html", context=options)
