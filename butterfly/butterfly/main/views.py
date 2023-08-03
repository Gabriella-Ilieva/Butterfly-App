from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from butterfly.initiatives.models import Initiative
from butterfly.main.forms import CommentForm
from butterfly.main.models import Comment


def index(request):

    return render(request, 'index.html')


# @login_required
# def comment_functionality(request, pk):
#     initiative = Initiative.objects.get(pk=pk)
#     new_comment_instance = None
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             print('valid')
#             new_comment_instance = form.save(commit=False)
#             new_comment_instance.to_initiative = initiative
#             new_comment_instance.user = request.user
#             new_comment_instance.save()
#             return redirect(request.META['HTTP_REFERER'])
#         else:
#             print('invalid')
#     else:
#         form = CommentForm(request.GET)
#
#     context = {
#         'initiative': initiative,
#         'new_comment_instance': new_comment_instance,
#         'comment_form': form,
#     }
#
#     return render(request, 'initiative/details_initiative.html', context)

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
