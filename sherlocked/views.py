from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Question
from userAuth.models import Player

import datetime


@login_required
def dashboard(request):
    player = Player.objects.get(username=request.user.username)
    return HttpResponse("Hello, {}. This is the dashboard. You are at level {}"\
        .format(player.username, player.level))

@login_required
def play(request):
    # user submitted an answer to a question
    player = Player.objects.get(username=request.user.username)
    question = Question.objects.get(question_level=player.level)

    question_text = question.question_text
    question_story = question.question_story
    question_level = question.question_level
    
    context = {
        'question_text': question_text,
        'question_story': question_story,
        'question_level': question_level, 
    }

    return render(
        request,
        'sherlocked/play.html',
        context
    )

def submit(request):
    if request.method == 'POST':

        is_correct = 'false'
        response_text = 'Wrong Answer! Please try again!'

        player = Player.objects.get(username=request.user.username)
        question = Question.objects.get(question_level=player.level)
        if question.answer.lower() == str(request.POST.get("answer")):

            # TODO: Add a check for winning condition

            # Increment the level of player if last question is not reached
            player.level = player.level + 1
            player.save()

            is_correct = 'true'
            response_text = 'Correct Answer!'

        return JsonResponse(
            {
                'isCorrect': is_correct,
                'responseText': response_text,
            }
        )
    return redirect("play")