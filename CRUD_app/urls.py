from CRUD_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar', views.cria, name='cadastrar'),
    path('listar', views.listar, name='listar'),
    path('excluir/<int:pk>', views.excluir, name='excluir'),
    path('editar/<int:pk>', views.editar, name='editar'),
]
