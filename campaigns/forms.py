from django import forms

from campaigns.models import Campaign


class CampaignForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Campaign
        fields = ["name", "language"]
