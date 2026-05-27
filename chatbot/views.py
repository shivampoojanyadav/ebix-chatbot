from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
import json

from .utils import get_best_answer


def home(request):
    return render(request, "chatbot/index.html")


def get_response(request):

    if request.method == "POST":

        data = json.loads(request.body)

        question = data.get("question")

        answer = get_best_answer(question)

        return JsonResponse({
            "answer": answer
        })

    return JsonResponse({
        "answer": "Invalid request"
    })