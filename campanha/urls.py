from django.urls import path
from . import views

urlpatterns = [
    # Sistema de Login
    path('login/', views.login_view, name='login'),

    # Página Inicial (opcional)
    path('', views.home, name='home'),

    # Agenda
    path('eventos/', views.listar_eventos, name='eventos'),
    path('eventos/criar/', views.criar_evento, name='criar_evento'),
    path('eventos/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('eventos/deletar/<int:evento_id>/', views.deletar_evento, name='deletar_evento'),

    # Logística
    path('logistica/recursos/', views.listar_recursos, name='listar_recursos'),
    path('logistica/recursos/criar/', views.criar_recurso, name='criar_recurso'),
    path('logistica/planejamento/', views.planejamento_rotas, name='planejamento_rotas'),

    # Marketing
    path('marketing/materiais/', views.listar_materiais, name='listar_materiais'),
    path('marketing/materiais/aprovar/<int:material_id>/', views.aprovar_material, name='aprovar_material'),

    # Demandas
    path('demandas/', views.listar_demandas, name='listar_demandas'),
    path('demandas/criar/', views.criar_demanda, name='criar_demanda'),
    path('demandas/<int:demanda_id>/', views.detalhe_demanda, name='detalhe_demanda'),
    
    # Materiais
    path('materiais/', views.listar_materiais, name='listar_materiais'),
    path('materiais/criar/', views.criar_material, name='criar_material'),
    path('materiais/editar/<int:material_id>/', views.editar_material, name='editar_material'),
    path('materiais/aprovar/<int:material_id>/', views.aprovar_material, name='aprovar_material'),
    path('materiais/deletar/<int:material_id>/', views.deletar_material, name='deletar_material'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),  # Adiciona a URL para o Dashboard
    
    # Coordenadores/lideres/eleitor
    path('coordenadores/', views.listar_coordenadores, name='listar_coordenadores'),
    path('liderancas/', views.listar_liderancas, name='listar_liderancas'),
    path('eleitores/', views.listar_eleitores, name='listar_eleitores'),
]
