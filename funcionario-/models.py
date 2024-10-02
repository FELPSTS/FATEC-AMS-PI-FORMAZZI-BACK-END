from django.db import models

class FUNCIONARIO(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    empresa_pertence = models.CharField(max_length=255)
    id_empresa_pertence = models.CharField(max_length=255)
    adm_responsavel = models.CharField(max_length=255)
    id_adm_responsavel = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
