from django.db import models

# Create your models here.


class Departamento(models.Model):
    sigla = models.CharField(max_length=6)
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.descricao}"


class Cachorro(models.Model):
    tem_cachorro = models.BooleanField()
    nome_do_cahorro = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome_do_cahorro}"


class PessoaEspecial(models.Model):
    especial = models.BooleanField()
    nome_deficiencia = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome_deficiencia}"


class PessoaManager(models.Manager):
    """
    Retorna maiores de 18
    """

    def obter_pessoas_adultas(self):
        result = Pessoa.objects.filter(idade__gte=18)
        return result


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField(null=True)

    depto_atual = models.ForeignKey(
        Departamento, on_delete=models.RESTRICT, null=True)

    hist_deptos = models.ManyToManyField(
        Departamento, related_name="hist_pessoa_depto")

    depto_chefia = models.OneToOneField(
        Departamento, on_delete=models.RESTRICT, null=True, related_name="chefia_depto"
    )

    ESCOLARIDADE_CHOICES = [
        ("NI", "Não informado"),
        ("EF", "Ensino Fundamental"),
        ("EM", "Ensino Médio"),
        ("ES", "Ensino Superior"),
    ]

    escolaridade = models.CharField(
        max_length=2, choices=ESCOLARIDADE_CHOICES, default="NI"
    )

    tem_cachorro = models.ForeignKey(
        Cachorro, on_delete=models.RESTRICT, null=True)

    especial = models.ForeignKey(
        PessoaEspecial, on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return f"{self.nome} ({self.id})"

    objects = PessoaManager()
