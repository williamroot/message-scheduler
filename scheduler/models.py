from django.db import models
from model_utils import Choices


class CommunicationScheduling(models.Model):
    """
    Model responsável por armazenar os agendamentos de
    envio de comunicação
    """
    MESSAGE_TYPES = Choices(
        ('sms', 'Mensagem SMS'),
        ('sending', 'Mensagem Whatsapp'),
        ('push', 'Notificação Push'),
        ('email', 'E-mail')
    )
    STATUS = Choices(
        ('waiting', 'Aguardando'),
        ('running', 'Executando envio'),
        ('done', 'Envio realizado'),
        ('error', 'Erro')
    )
    created_at = models.DateTimeField(
        'Data/hora de criação do agendamento',
        auto_now_add=True
    )
    status = models.CharField(
        'Status do agendamento',
        choices=STATUS,
        max_length=7,
        null=False,
        default=STATUS.waiting
    )
    message_type = models.CharField(
        'Tipo de mensagem',
        choices=MESSAGE_TYPES,
        max_length=8,
        null=False,
        blank=False
    )
    scheduling = models.DateTimeField(
        'Data/hora de agendamento para envio',
        null=False,
        blank=False
    )
    message = models.TextField(
        'Mensagem a ser entregue',
        null=False,
        blank=False
    )
    recipient = models.TextField(
        'Destinatário de mensagem',
        null=False,
        blank=False
    )
