from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Modelo de Usuário
class Usuario(AbstractUser):
    tipo_choices = [
        ('coordenador', 'Coordenador'),
        ('lideranca', 'Liderança'),
        ('eleitor', 'Eleitor'),
    ]
    tipo = models.CharField(max_length=20, choices=tipo_choices)

    # Evitando conflitos de relacionamento
    groups = models.ManyToManyField(
        Group,
        related_name="usuario_groups",  # Renomeia o campo relacionado
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuario_permissions",  # Renomeia o campo relacionado
        blank=True
    )

# Modelo de Agenda
class Agenda(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_horario = models.DateTimeField()
    criado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# Modelo de Eventos
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=150)
    data_horario = models.DateTimeField()

# Outros modelos (Logística, Marketing e Demandas)
# (Podem ser definidos de maneira semelhante)

class Logistica(models.Model):
    tipo_recurso_choices = [
        ('transporte', 'Transporte'),
        ('alimentacao', 'Alimentação'),
        ('material_grafico', 'Material Gráfico'),
    ]
    tipo_recurso = models.CharField(max_length=20, choices=tipo_recurso_choices)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo_recurso} - {self.descricao}"

class MaterialMarketing(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Demanda(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_por = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pendente')

    def __str__(self):
        return self.titulo
