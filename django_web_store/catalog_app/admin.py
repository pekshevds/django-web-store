from django.contrib import admin

from catalog_app.models import Category
from catalog_app.models import Good


class GoodAdmin(admin.ModelAdmin):
    pass


class InlineGoodlAdmin(admin.StackedInline):
    model = Good


class CatergryAdmin(admin.ModelAdmin):

    list_display = ('name', 'parent', )
    list_filter = ('parent', )
    inlines = (InlineGoodlAdmin, )


admin.site.register(Category, CatergryAdmin)
admin.site.register(Good, GoodAdmin)
