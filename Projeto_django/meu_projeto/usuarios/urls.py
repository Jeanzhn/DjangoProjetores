from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TabelaGeralView, confirmar_reserva, reservar_datashow, adicionar_datashow, registrar, index, logout, adicionar_professor, tabela_professores, home, remover_professor, AluguelView


urlpatterns = [ 
    #Tela inicial e registro
    path('', index, name='index'),
    path('registrar/', registrar, name='registrar'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', logout, name='logout'),
    path('home', home, name ='home' ),

    #orienteção e gestão de professores
    path('adicionar/', adicionar_professor, name='adicionar_professor'),
    path('tabela/', tabela_professores, name='tabela_professor'),
    path('remover_user/<int:user_id>/', remover_professor, name='remover_Professor'),

    #orientação e gestão de datashow
    path('adicionar_datashow/', adicionar_datashow, name='adicionar_datashow'),
    path('reservar/<int:datashow_id>/', reservar_datashow, name='reservar_datashow'),
    path('confirmar_reserva/<int:datashow_id>/', confirmar_reserva, name='confirmar_reserva'),

    #aluguel e mostrar reservados
    path('tabela_geral/', TabelaGeralView.as_view(), name='tabela_geral'),
    path('aluguel/', AluguelView.as_view(), name='aluguel'),
    
]
