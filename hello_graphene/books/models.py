from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    birth_year = models.SmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', '-birth_year')


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ManyToManyField(Author)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
