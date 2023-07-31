from django import forms

from butterfly.stories.models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'description', 'image']


class EditStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'description', 'image']

    # def save(self, commit=True):
    #     story = Story.objects.get(pk=self.instance.id)
        # if commit:
        #     image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
        #     os.remove(image_path)
        # return super().save(commit)



