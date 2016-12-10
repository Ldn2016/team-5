from django.db import models


"""This defines the fields and entities in our database.

The database is a simple relational database representing a many-to-many relationship between books and stores.

A store can have multiple books, while a book can be in multiple stores.

The entity 'quantity' bridges this relationship and represents a single book in a store.

"""


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
    item = models.ForeignKey(Book, on_delete=models.CASCADE) #On deletion of an object in this class, everything connected to it is also deleted.
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "{} | {} | {}".format(self.store, self.item, self.amount)
