from django.db import models
import datetime


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    @staticmethod
    def checkUser(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_id(id):
        return Customer.objects.filter(id=id)


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class UploadImages(models.Model):
    gallery_name = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Gallery')
