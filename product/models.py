from django.db import models

# Create your models here.

class Category(models.Model):
    cat_title = models.CharField(max_length=20)
    description = models.TextField(max_length=30)  

    def __str__(self):
        return self.cat_title
    
    def get_all_categories():
        return Category.objects.all()


class Shop(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    image = models.ImageField(upload_to ='images', default='images/me.jpeg')

    def __str__(self):
        return self.title


class Product(models.Model):
    prod = models.ForeignKey(Shop, on_delete=models.CASCADE, default = 1)
    prod_ids = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=100)
    amount = models.IntegerField()
    images = models.ImageField(upload_to ='images')
    active = models.BooleanField()

    # def get_products_by_id(prod_ids):
    #     return Product.objects.filter(id__in =prod_ids)


    # def get_all_products():
    #     return Product.objects.all()

    # def get_all_products_by_categoryid(category_id):
    #     if category_id:
    #         return Product.objects.filter(category = category_id)
    #     else:
    #         return Product.get_all_products()


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)