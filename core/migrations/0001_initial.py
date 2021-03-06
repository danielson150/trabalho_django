# Generated by Django 2.1.4 on 2018-12-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='data do evento')),
                ('hora', models.TimeField()),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'tarefa agendada',
                'verbose_name_plural': 'tarefas agendadas',
            },
        ),
    ]
