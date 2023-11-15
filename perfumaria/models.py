from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Marca (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Perfume(models.Model):
    nome = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    data_fabricacao = models.CharField(max_length=8)
    imagem = models.ImageField(upload_to='perfume_img/')

    def __str__(self):
        return self.nome




