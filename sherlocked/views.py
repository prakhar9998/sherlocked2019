from django.shortcuts import HttpResponse, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import PlayerCreationForm
from .models import Player, Question

class SignUp(generic.CreateView):
    form_class = PlayerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

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
    
    if request.method=='POST':
        if question.answer.lower() == str(request.POST.get("answer")):
            # TODO: Add a check for winning condition
            # Increment the level of player if last question is not reached
            player.level = player.level + 1
            player.save()

            # fetch next question to display if answer is correct
            question = Question.objects.get(question_level=player.level)

    question_text = question.question_text
    question_story = question.question_story
    question_level = question.question_level

    return render(
        request,
        'sherlocked/play.html',
        {
            'question_text': question_text,
            'question_story': question_story,
            'question_level': question_level,
        }
    )
