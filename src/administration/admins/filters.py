import django_filters
from django.forms import TextInput

from src.administration.admins.models import Property


class PropertyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Name'}))

    class Meta:
        model = Property
        fields = {
            'city'
        }