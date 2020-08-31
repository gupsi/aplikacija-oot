import django_filters
from .models import *

class SFilter(django_filters.FilterSet):
	class Meta:
		model = OdradjeniSati
		fields =  {
		'datum':['exact'],
		}
