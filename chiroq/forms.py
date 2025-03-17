from django import forms
from .models import Chiroq

class ChiroqForm(forms.ModelForm):
    class Meta:
        model = Chiroq
        fields = '__all__'