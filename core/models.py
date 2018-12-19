from django.db import models

class ItemAgenda(models.Model):
    data = models.DateField('data do evento')
    hora = models.TimeField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'tarefas agendadas'
        verbose_name = 'tarefa agendada'


        def __str__(self):
            return '{} {} {} {}'.format(
                    self.data.strftime('%d/%m/%Y'),
                    self.hora.strftime('%H:%M'),
                    self.titulo,
                    self.criado_em

            )