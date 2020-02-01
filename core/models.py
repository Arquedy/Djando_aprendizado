# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now = True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    

    class Meta:
        pass
    def __str__(self):
            return self.titulo
