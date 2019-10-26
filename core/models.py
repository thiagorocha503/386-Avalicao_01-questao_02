from django.db import models


# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField("Carga horária")
    ementa = models.TextField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ("nome", "valor")


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    valor_hora_aula = models.DecimalField("Valor hora/aula", max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    data_inicio = models.DateField("Data de ínicio")
    data_termino = models.DateField("Data de término")
    hora_inicio = models.TimeField("Horário do ínicio")
    hora_termino = models.TimeField("Hórario do término")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.curso.nome,
                            self.data_inicio.strftime("%d/%m/%Y")
                            )

    class Meta:
        ordering = ("data_inicio", "data_termino")
