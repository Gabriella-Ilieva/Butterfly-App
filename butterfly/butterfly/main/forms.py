from django import forms

from butterfly.main.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...'
                }),
        }


class SearchForm(forms.Form):
    title_filed = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by title...'
            }
        )
    )
