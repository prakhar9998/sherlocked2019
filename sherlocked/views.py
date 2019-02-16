"""
Contains views for the sherlocked app.
"""

from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from userAuth.models import Player
from .models import Question


@login_required
def dashboard(request):

    """
    Player dashboard containing the basic info like
    the level user is at.
    """

    player = Player.objects.get(username=request.user.username)
    return HttpResponse("Hello, {}. This is the dashboard. You are at level {}"\
        .format(player.username, player.level))

@login_required
def play(request):

    """
    This method will render the question according to
    the no. of question a player have solved. The submit url
    also redirects to this question.
    """

    player = Player.objects.get(username=request.user.username)
    question = Question.objects.get(question_level=player.level)

    context = {
        'question': question,
    }

    return render(
        request,
        'sherlocked/play.html',
        context
    )

def submit(request):

    """
    This method is called after a user submits the answer.
    The answer gets validated through this method and if the
    answer is correct the player's level is increased.
    """

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
