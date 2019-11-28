from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(
        max_length=50
    )

    SEXO_CHOICE = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICE,
    )

    funcao = models.CharField(
        max_length=50
    )

    salario = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
