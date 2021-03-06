# Generated by Django 3.1.2 on 2020-10-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20201011_0046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communicationscheduling',
            options={'verbose_name': 'Agendamento', 'verbose_name_plural': 'Agendamentos'},
        ),
        migrations.AlterField(
            model_name='communicationscheduling',
            name='status',
            field=models.CharField(blank=True, choices=[('waiting', 'Aguardando'), ('running', 'Executando envio'), ('done', 'Envio realizado'), ('error', 'Erro')], default='waiting', max_length=7, verbose_name='Status do agendamento'),
        ),
    ]
