from django import forms
from .models import Venue, Show


class ShowForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Show name here'}))
    name2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Show name here'}))

    class Meta:
        model = Show
        fields = ('artists', 'venue', 'show_time', 'photo')
        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'show name'})
        # }


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'city', 'state', 'country', 'address', 'telephone')