from django.db import models
from model_utils import Choices


class CommunicationScheduling(models.Model):
    """
    Model responsável por armazenar os agendamentos de
    envio de comunicação
    """
    MESSAGE_TYPES = Choices(
        ('sms', 'Mensagem SMS'),
        ('whatsapp', 'Mensagem Whatsapp'),
        ('push', 'Notificação Push'),
        ('email', 'E-mail')
    )
    created_at = models.DateTimeField(
        'Data/hora de criação do agendamento',
        auto_now_add=True
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
