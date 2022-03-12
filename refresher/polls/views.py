from django.http import Http404
from django.shortcuts import render
from .models import Question, Choice

# Get and display questions
def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]

    context = {"latest_questions": latest_questions}

    return render(request, "polls/index.html", context)


def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question not found!")

    return render(request, "polls/details.html", {"question": question})
