from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Category", max_length=150, primary_key=True)
    parent = models.ForeignKey("Category", related_name="childs", blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Good(models.Model):
    name = models.CharField(verbose_name="Good", max_length=150, primary_key=True)
    category = models.ForeignKey("Category", related_name="goods", blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name
