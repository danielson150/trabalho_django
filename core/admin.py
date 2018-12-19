from django.contrib import admin
from core.models import ItemAgenda

admin.site.register(ItemAgenda)

admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'Minhas Tarefas'
