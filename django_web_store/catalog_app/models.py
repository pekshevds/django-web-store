from django.db import models


class AbstractModel(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        abstract = True


class Category(AbstractModel):
    name = models.CharField(verbose_name="Category", max_length=150, db_index=True)
    code = models.CharField(verbose_name="code", max_length=11, db_index=True, default='')
    parent = models.ForeignKey("Category", related_name="childs", blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def fetch_top_level_categories(cls):
        return cls.objects.filter(parent=None)

    @property
    def fetch_childs(self):
        return Category.objects.filter(parent=self)


class Good(AbstractModel):
    name = models.CharField(verbose_name="Good", max_length=150, db_index=True)
    code = models.CharField(verbose_name="code", max_length=11, db_index=True, default='')
    category = models.ForeignKey("Category", related_name="goods", blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name
