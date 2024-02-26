
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views


app_name = 'todos'

urlpatterns = [
    path("", auth_views.LoginView.as_view(), name='login'),
    path("home/", views.home, name='home'),
    path('posts/<int:postagem_id>', views.postagem),  
    path('conteudos/<int:postagem_id>/', views.todos_conteudos, name='todos_conteudos'),
    path('conteudos/<int:conteudo_id>/', views.conteudo, name='conteudo'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
   
]