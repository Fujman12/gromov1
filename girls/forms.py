from django import forms


HAIR_CHOICES =[
    ("All", "All"),
    ("Light brown", "Light brown"),
    ("Brunette", "Brunette"),
    ("Blonde", "Blonde"),
    ("Redhead", "Redhead")
]


class SearchForm(forms.Form):
    age_from = forms.IntegerField(min_value=16,
                                  max_value=80,
                                  widget=forms.NumberInput(attrs={'placeholder': 'From'}),
                                  required=False)
    age_to = forms.IntegerField(min_value=16,
                                max_value=80,
                                widget=forms.NumberInput(attrs={'placeholder': 'TO'}),
                                required=False)

    hair_choice = forms.ChoiceField(choices=HAIR_CHOICES)
