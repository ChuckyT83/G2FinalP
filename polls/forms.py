from django.forms import ModelForm
from .models import Question

class CreatePollForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'answerOne', 'answerTwo']