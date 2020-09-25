from django.urls import path
from . import views

urlpatterns = [
    path("", views.createPessoa, name="Home"),
    path("editar/", views.editPessoa, name="Edit"),
    path("deletar/", views.deletePessoa, name="Deletar"),
    path("pessoa/<int:idpessoa>/", views.pessoa, name="pessoa"),
    path("lista_pessoas/", views.lista_pessoas, name="lista_pessoas"),
    path(
        "create/<str:nome>/<str:sobrenome>/<int:idade>/<str:escolaridade>/<str:dpto_descricao>/",
        views.create,
        name="create",
    ),
    path("update/<int:id>/<str:dpto_descricao>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
]
