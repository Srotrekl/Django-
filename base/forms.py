from django.forms import ModelForm

from base.models import room


class RoomForm(ModelForm):
    class Meta:
        model=room
        fields = '__all__'
        exclude = ['participants']


