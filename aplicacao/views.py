from .models.Form import FormularioPessoa, FormularioEditarDepartamento, FormularioDeletarPessoa
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models.Pessoa import Pessoa, Departamento
from django.template import loader


def pessoa(request, idpessoa):
    p = Pessoa.objects.get(pk=idpessoa)
    dados = {"pessoa": p}
    return render(request, "pessoa/detalhar.html", dados)


def lista_pessoas(request):
    # Aqui é o modelo
    lista_p = Pessoa.objects.obter_pessoas_adultas()
    dados = {"listapessoas": lista_p}

    # Aqui é o template
    template = loader.get_template("pessoa/listar.html")
    return HttpResponse(template.render(dados, request))


def create(request, nome, sobrenome, idade, escolaridade, dpto_descricao):
    novoDepartamento = Departamento(
        sigla=dpto_descricao[0].upper(), descricao=dpto_descricao.upper()
    )
    novoDepartamento.save()
    novaPessoa = Pessoa(
        nome=nome,
        sobrenome=sobrenome,
        idade=idade,
        escolaridade=escolaridade,
        depto_chefia_id=novoDepartamento.id,
    )
    novaPessoa.depto_atual_id = novoDepartamento.id
    novaPessoa.save()


def update(request, nome, dpto_descricao):
    novoDepartamento = Departamento(
        sigla=dpto_descricao[0].upper(), descricao=dpto_descricao.upper()
    )
    novoDepartamento.save()
    pessoa = Pessoa.objects.get(nome=nome)
    pessoa.depto_atual_id = novoDepartamento.id
    pessoa.save()


def delete(request, nome):
    Pessoa.objects.get(nome=nome).delete()


def createPessoa(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormularioPessoa(request.POST)
        # check whether it's valid:
        if form.is_valid():

            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            idade = form.cleaned_data['idade']
            escolaridade = form.cleaned_data['escolaridade']
            depto = form.cleaned_data['depto']

            create(request, nome, sobrenome, idade, escolaridade, depto)

            return JsonResponse({"pessoa_criada": form.cleaned_data})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormularioPessoa()

    return render(request, "pessoa/home.html", {'form': form})


def editPessoa(request):
    if request.method == 'POST':
        form = FormularioEditarDepartamento(request.POST)

        if form.is_valid():

            nome = form.cleaned_data['nome']
            novo_departamento = form.cleaned_data['novo_departamento']

            update(request, nome, novo_departamento)

            return JsonResponse({"pessoa_editada": form.cleaned_data})

    else:
        form = FormularioEditarDepartamento()

    return render(request, "pessoa/editarDepartamento.html", {'form': form})


def deletePessoa(request):
    if request.method == 'POST':
        form = FormularioDeletarPessoa(request.POST)

        if form.is_valid():

            nome = form.cleaned_data['nome']

            delete(request, nome)

            return JsonResponse({"pessoa_excluída": form.cleaned_data})

    else:
        form = FormularioDeletarPessoa()

    return render(request, "pessoa/deletarPessoa.html", {'form': form})
