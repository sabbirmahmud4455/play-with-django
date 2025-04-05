from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
	latest_question_list =  Question.objects.order_by("-pub_date")[:5]
	latest_question_list = ", ".join([str(q) for q in latest_question_list])

	context = {
		"latest_question_list": latest_question_list,
	}

	return render(request, "polls/index.html", context)

	return HttpResponse(latest_question_list)

def detail(request, question_id):
	return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
	return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
	return HttpResponse(f"You're voting on question {question_id}.")

