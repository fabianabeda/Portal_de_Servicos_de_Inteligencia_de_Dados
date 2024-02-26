from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Postagem(models.Model):
    POSTAGEM_STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Rascunho')
    )
    
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='postagem_images/', null=True, blank=True)
    status = models.CharField(max_length=15, choices=POSTAGEM_STATUS)
    atualizacao = models.DateTimeField(auto_now=True)
    versao = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Conteudo(models.Model):
    CONTEUDO_STATUS = (
        ('active', 'Ativo'),
        ('draft', 'Rascunho')
    )
    title = models.CharField(max_length=255)
    summary = RichTextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='conteudo_images/', null=True, blank=True)
    site_link = models.URLField(max_length=255)
    status = models.CharField(max_length=15, choices=CONTEUDO_STATUS)
    
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='conteudos')

    def __str__(self):
        return self.title
