from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/category/',default=None,editable=True,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Slider(models.Model):
    main_title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/sliders/',default=None,editable=True)
    url = models.URLField(blank=True,null=True,default=None)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.main_title)



class Size(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)

class Color(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='product_category')
    size = models.ManyToManyField(Size,blank=True,null=True, related_name="product_size")
    color = models.ManyToManyField(Color,blank=True,null=True, related_name="product_color")
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/products/',default=None,editable=True)
    price = models.FloatField()
    offer_price = models.FloatField(blank=True,null=True)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False,default=None,null=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class ProductSlider(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE,related_name='product_slider_images')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/sliders/',default=None,editable=True)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.title)

class Sku(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Stocks Keeping Units'



class Favourite(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='fav')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=False,default=None,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Favourites'
