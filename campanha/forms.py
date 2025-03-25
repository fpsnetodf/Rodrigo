from django import forms
from .models import Evento, Logistica, Demanda, MaterialMarketing
from django.utils import timezone



# Formulário para Evento
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'local', 'data_horario']

    def clean_data_horario(self):
        data_horario = self.cleaned_data['data_horario']
        if data_horario < timezone.now():
            raise forms.ValidationError('A data e hora do evento não podem estar no passado.')
        return data_horario

# Formulário para Recurso Logístico
class RecursoForm(forms.ModelForm):
    class Meta:
        model = Logistica
        fields = ['tipo_recurso', 'descricao', 'quantidade', 'disponivel']

# Formulário para Demanda
class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['titulo', 'descricao', 'status']


# Materiais
class MaterialMarketingForm(forms.ModelForm):
    class Meta:
        model = MaterialMarketing
        fields = ['nome', 'descricao']
