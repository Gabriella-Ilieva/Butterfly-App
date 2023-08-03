from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from butterfly.initiatives.models import Initiative
from butterfly.main.forms import CommentForm
from butterfly.main.models import Comment


def index(request):

    return render(request, 'index.html')


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
