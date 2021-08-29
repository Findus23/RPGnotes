from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

from days.models import Session, IngameDay


class DayForm(ModelForm):
    sessions = ModelMultipleChoiceField(
        queryset=Session.objects.all(),
        widget=CheckboxSelectMultiple()
    )

    class Meta:
        model = IngameDay
        fields = ["day", "description_md", "sessions"]
