from django.db import models

from datetime import datetime


class Company(models.Model):

    name = models.CharField(max_length=20, default='company name')
    description = models.TextField(default='')
    article = models.IntegerField(default=0, null=False)

    def __str__(self):
        return '{}'.format(self.name)


class Category(models.Model):

    name = models.CharField(max_length=20, default='category name')
    article = models.IntegerField(default=0, null=False)

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):

    name = models.CharField(max_length=20, null=False)
    description = models.TextField(default='')
    description_short = models.TextField(default='')
    price = models.CharField(max_length=20, default=0, null=False)
    price_opt = models.CharField(max_length=20, default=0, null=False)
    image = models.ImageField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    article = models.IntegerField(default=0, null=False)

    def __str__(self):
        return '{} [{}]'.format(self.name, self.company.name)
