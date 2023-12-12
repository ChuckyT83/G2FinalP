from django.forms import ModelForm, RadioSelect
from .models import Question

class Ch(ModelForm):
    class Meta:
        model = Question
        fields = ['answerOne', 'answerTwo']
        widget = RadioSelect()