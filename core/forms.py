from django import forms
from .models import Venue, Show


class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ('artists', 'name', 'venue', 'show_time', 'photo')


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'city', 'state', 'country', 'address', 'telephone')