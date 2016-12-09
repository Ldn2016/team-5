from django.db import models


class Item(models.Model):
    id_number = models.IntegerField()

    def __str__(self):
        return str(self.id_number)


class Book(Item):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class CD(Item):
    title = models.CharField(max_length=1000)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Store(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Quantity(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # TODO: figure out what models.CASCADE is for
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    amount = models.IntegerField()
