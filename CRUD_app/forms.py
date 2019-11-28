from .models import Funcionario
from django.forms import ModelForm

class InsertFuncionario(ModelForm):

    class Meta:
        model = Funcionario
        fields = '__all__'