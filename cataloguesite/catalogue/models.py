from django.db import models


class Book(models.Model):
    id_number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    thumbnail = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.id_number)


class Store(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.name, self.pk)


class Quantity(models.Model):
    item = models.ForeignKey(Book, on_delete=models.CASCADE)  # TODO: figure out what models.CASCADE is for
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "{} | {} | {}".format(self.store, self.item, self.amount)
