from django.forms import ModelForm, RadioSelect
from .models import Question

class SurveyForm(ModelForm):
    class Meta:
        model = Question
        fields = ['answerOne', 'answerTwo']
        widget = RadioSelect()