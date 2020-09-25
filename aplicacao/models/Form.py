from django import forms


class FormularioPessoa(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    sobrenome = forms.CharField(label='Sobrenome', max_length=100)
    idade = forms.CharField(label='Idade', max_length=3)
    escolaridade = forms.CharField(
        label='Escoloridade', max_length=20)
    depto = forms.CharField(label='Departamento')


class FormularioEditarDepartamento(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    novo_departamento = forms.CharField(
        label='Novo departamento', max_length=100)


class FormularioDeletarPessoa(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
