from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class LandingSlider(models.Model):
    slider_img = models.ImageField(upload_to="images/")

    def __str__(self):

        return str(self.id)



class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_text = models.CharField(max_length=1000)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.user)


class DummyUser(models.Model):
    user = models.CharField(max_length=120, default=None)

    def __str__(self):
        return self.user



class Services(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=120)
    img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.sub_title


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    icon = models.FileField(upload_to="images/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg', 'png'])], null=True)


    def __str__(self):
        return self.title


class Subcategory(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    parent_market = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

class Tag(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)


    def __str__(self):
        return self.title

class DeliveryTime(models.Model):
    title = models.CharField(max_length=120)


    def __str__(self):
        return self.title


class Package(models.Model):
    title = models.CharField(max_length=120)
    
    
    def __str__(self):
        return self.title
    

class Gig(models.Model):
    gig_title = models.CharField(max_length=240)
    image = models.ImageField(upload_to='images/')
    extra_images = models.ImageField(upload_to="images/")
    gig_video = models.FileField(upload_to="images/")
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    packages = models.ManyToManyField(Package, through='GigManager')
    
    
    def __str__(self):
        return self.gig_title
    
    
class GigManager(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)




class PostRequestModel(models.Model):
    post_rqst_slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    attachment = models.FileField(upload_to="files/", null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.DO_NOTHING, null=True)
    delivery_time = models.ForeignKey(DeliveryTime, on_delete=models.DO_NOTHING, null=True)
    budget = models.FloatField()


    def __str__(self):
        return self.title


class Currency(models.Model):
    currency_name = models.CharField(max_length=100)

    def __str__(self):
        return self.currency_name


class Rating(models.Model):
    title = models.CharField(max_length=120)


    def __str__(self):
        return self.title



class ReviewSeller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True)
    rate_seller = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)


