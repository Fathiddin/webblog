from django.forms import ModelForm
from .models import *

# Add new book form


class AddPersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ["image", "name", "phone", "mail", "telegram", "slug", "body"]
        