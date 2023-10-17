from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    questions = Question.objects.all()
    options = {
        "questions": questions
    }

    return render(request, template_name="pages/index.html", context=options)


def detail(request):
    name = request.GET.get('name', '')
    context = {
        "name": name
    }
    return render(request, template_name="pages/doc_detail.html", context=context)