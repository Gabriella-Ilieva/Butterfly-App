from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from butterfly.accounts.models import ButterflyUser
from butterfly.initiatives.models import Initiative, Participation
from butterfly.main.forms import CommentForm
from butterfly.main.models import Comment
from butterfly.stories.models import Story


def index(request):
    initiatives_count = Initiative.objects.all().count()
    participants_count = Participation.objects.all().count()
    users_count = ButterflyUser.objects.all().count()
    all_stories = Story.objects.all()
    stories_list = all_stories[0:6]
    stories_count = all_stories.count()
    context = {
        'stories': stories_list,
        'stories_count': stories_count,
        'initiatives_count': initiatives_count,
        'participants_count': participants_count,
        'users_count': users_count,
    }
    return render(request, 'index.html', context)


@login_required
def comment_functionality(request, initiative_pk):
    if request.method == 'POST':
        initiative = Initiative.objects.get(pk=initiative_pk)
        user = request.user
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.to_initiative = initiative
            new_comment.user = user
            new_comment.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{initiative_pk}")
