from django.db import models

# Create your models here.

class emprestimo(models.Model):
    data_emprestimo = models.CharField(max_length=100)
    data_devolucao = models.CharField(max_length=100)
    leitor = models.ForeignKey('leitor', on_delete=models.CASCADE)
    livro = models.ForeignKey('livro', on_delete=models.CASCADE)
    bibliotecario = models.ForeignKey('blibliotecario', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.data_emprestimo

class leitor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=12)

    def __str__(self):
        return self.nome

class blibliotecario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=12)

    def __str__(self):
        return self.nome

class livro(models.Model):
    titulo = models.CharField(max_length=100)
    ano_publicacao = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    categoria = models.ForeignKey('categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class categoria(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome

