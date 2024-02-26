from django.contrib import admin

from todos.models import Conteudo, Postagem

admin.site.register(Postagem)
admin.site.register(Conteudo)