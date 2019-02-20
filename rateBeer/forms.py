from django import forms

from .models import Taste

class TasteForm(forms.ModelForm):

    class Meta:
        model = Taste
        fields = ('brewery', 'beer_name', 'beer_type', 'abv', 'purchased_location', 'rating', 'tasting_notes')