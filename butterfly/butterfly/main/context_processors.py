from butterfly.initiatives.models import Participation, Initiative
from butterfly.stories.models import Story


def user_properties(request):
    if request.user.is_authenticated:
        participation_count = Participation.objects.filter(user=request.user).count()
        user_participation = Participation.objects.filter(user=request.user)
        story_count = Story.objects.filter(user=request.user).count()
        user_stories = Story.objects.filter(user=request.user)
        initiative_count = Initiative.objects.filter(user=request.user).count()
        user_initiatives = Initiative.objects.filter(user=request.user)

        context = {
            'participation_count': participation_count,
            'story_count': story_count,
            'initiative_count': initiative_count,
            'user_participation': user_participation,
            'user_initiatives': user_initiatives,
            'user_stories': user_stories,
        }
    else:
        context = {}

    return context
