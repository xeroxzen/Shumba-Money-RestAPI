from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer


class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = UserCreationForm.Meta.fields + ('phone_number', 'country_of_residence', )

class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = UserChangeForm.Meta.fields
