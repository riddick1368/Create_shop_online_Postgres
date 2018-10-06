from django.db import models

# Create your models here.

class Brand(models.Model):
    title = models.CharField(unique=True,max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(unique=True,max_length=100)
    description = models.TextField(max_length=500)
    slug =models.SlugField()

    def __str__(self):
        return self.title


class Varations(models.Model):
    title = models.CharField(max_length=120)
    slug= models.SlugField()
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    sale_price = models.DecimalField(max_digits=15,decimal_places=2)
    product = models.ForeignKey('Product',on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        ordering =["-title"]


    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else :
            return self.price

# class ProductQueryset(models.QuerySet):
#
#     def get_related_product(self, instance):
#         return self.filter(category__in = instance)
#
#
# class ProductManger(models.manager):
#
#     def get_queryset(self):
#         return ProductQueryset(self.model,using=self._db)


class Product(models.Model):
    title = models.CharField(max_length=120,help_text="Enter uniqe title")
    hits = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    description = models.TextField(max_length=1500,help_text='descrip your Product')
    category = models.ManyToManyField(Category)
    active = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2,max_digits=15,help_text="قیمت ها به تومان می باشد.")


    def __str__(self):
        return self.title


    class Meta :
        ordering = ["-title"]




class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField()


    def __str__(self):
        return self.product.title



class ProductFeautre(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    hits = models.IntegerField(default=0)
    image = models.ImageField()
    title = models.CharField(max_length=120)
    text = models.TextField(max_length=15000)
    text_right = models.BooleanField(default=False)
    text_css_color = models.CharField(max_length=6, null=True, blank=True)
    show_price = models.BooleanField(default=False)
    make_image_background = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title
