from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple, DateInput

from days.models import Session, IngameDay


class DayForm(ModelForm):
    sessions = ModelMultipleChoiceField(
        queryset=Session.objects.all().order_by("-date"),
        widget=CheckboxSelectMultiple()
    )

    class Meta:
        model = IngameDay
        fields = ["day", "description_md", "sessions"]


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ["date"]
