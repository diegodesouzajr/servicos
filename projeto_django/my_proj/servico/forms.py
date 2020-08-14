from django import forms
from .models import ServicoUm


# creating a form
class ServicoUmForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = ServicoUm

        # specify fields to be used
        fields = [
            "numero_par",
        ]