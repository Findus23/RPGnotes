from django import forms


class CampaignForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
