from django.contrib import admin
from .models import *


# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "carga_horaria", "ementa", "valor")
    search_fields = ("nome",)


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'valor_hora_aula')
    search_fields = ('nome', 'telefone')


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('data_inicio', 'data_termino',
                    'hora_inicio', 'hora_termino',
                    'curso', 'professor')
    inline = ['curso', 'professor']
    list_filter = ('data_inicio', 'data_termino', 'curso', 'professor')
    date_hierarchy = 'data_inicio'


admin.site.site_title = "Empresa de curso profissionalizante"
admin.site.index_title = "Recursos"
admin.site.site_header = "Administração da Empresa"
admin.site.register(Curso, CursoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
