from django.db import models


book_choice = [('fiction','fiction'), ('drama','drama'), ('history','history'), ('children','children'),('college','college'), ('biography','biography')]


# Create your models here.
class Book(models.Model):
    book_id = models.AutoField
    auther = models.CharField(null=True, max_length=200)
    title = models.CharField(max_length=200)
    category = models.CharField(choices=book_choice, max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="home/images", default="")
    rating = models.CharField(max_length=10)
    review = models.CharField(max_length=200)


    def __str__(self):
        return self.title

# Create models for placing order.
class Order(models.Model):
    order_id = models.AutoField
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id = models.AutoField
    order_id =  models.IntegerField(default=" ", null= True)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "...."




