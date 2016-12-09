from django.db import models


class Item(models.Model):
    id_number = models.IntegerField()
    ITEM_KINDS = (
            ('BK', 'book'),
            ('CD', 'CD'),
            ('ZZ', 'other')
    )
    kind = models.CharField(max_length=2, choices=ITEM_KINDS)
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000, null=True, blank=True)

    other_data = models.CharField(max_length=10**4)

    def __str__(self):
        return str(self.id_number)


class Store(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Quantity(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # TODO: figure out what models.CASCADE is for
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return "{} | {} | {}".format(self.store, self.item, self.amount)
