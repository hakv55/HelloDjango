from django.forms import ModelForm
from visitsapi.models import Visit

class VisitsForm(ModelForm):

    class Meta:
        model = Visit
        fields = ['user_id', 'latitude', 'longitude', 'rate']
