import django_filters
from .models import *
from django_filters import DateFilter, CharFilter


class ContratoFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="fecha_inicio", lookup_expr='gte')
    end_date = DateFilter(field_name="fecha_terminacion", lookup_expr='lte')
    responsable = CharFilter(field_name="tecnico",)

    class Meta:
        model = Contrato
        fields = '__all__'
        exclude = ['cliente','print','tecnico', 'valor', 'nroContrato', 'equipo', 'fecha_creacion', 'fecha_inicio', 'fecha_terminacion']
