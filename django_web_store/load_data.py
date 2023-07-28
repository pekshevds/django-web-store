from catalog_app.models import Category
from catalog_app.models import Good
import csv

FILE_NAME = "catalog_data.csv"


def load_categories():
    categories = {}
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:

            item_name = row[0]
            item_code = row[1]
            is_category = row[2]
            parent_code = row[3]

            if is_category == "Да":
                if item_code not in categories.keys():
                    new_category = Category(name=item_name, code=item_code)
                    categories[item_code] = [item_name, new_category, parent_code]
    Category.objects.bulk_create([category[1] for category in categories.values()])


def load_goods():
    goods = {}
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:

            item_name = row[0]
            item_code = row[1]
            is_category = row[2]
            parent_code = row[3]

            if is_category == "Нет":
                if item_code not in goods.keys():
                    new_good = Good(name=item_name, code=item_code)
                    goods[item_code] = [item_name, new_good, parent_code]
    Good.objects.bulk_create([good[1] for good in goods.values()])


def load_data():

    load_categories()
    load_goods()
    # Category.objects.bulk_create(categories)
    # Good.objects.bulk_create(goods)


if __name__ == "__main__":
    load_data()
