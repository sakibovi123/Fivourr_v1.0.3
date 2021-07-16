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




class Gigs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gig_slug = models.SlugField(null=True)
    title = models.CharField(max_length=240)
    seo_title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag)
    # BASIC GIGS PACKAGE
    basic_title = models.CharField(max_length=120)
    basic_desc = models.CharField(max_length=240)
    basic_designCustom = models.BooleanField()
    basic_contentUp = models.BooleanField()
    basic_responsive = models.BooleanField()
    basic_plugins = models.IntegerField()
    basic_productsUp = models.IntegerField()
    basic_ecommerc = models.BooleanField()
    basic_revisions = models.IntegerField()
    basic_price = models.FloatField()

    # Standard Package
    standard_title = models.CharField(max_length=120)
    standard_desc = models.CharField(max_length=240)
    standard_designCustom = models.BooleanField()
    standard_contentUp = models.BooleanField()
    standard_responsive = models.BooleanField()
    standard_plugins = models.IntegerField()
    standard_productsUp = models.IntegerField()
    standard_ecommerc = models.BooleanField()
    standard_revisions = models.IntegerField()
    standard_price = models.FloatField()

    # PRemium Package

    premium_title = models.CharField(max_length=120)
    premium_desc = models.CharField(max_length=240)
    premium_designCustom = models.BooleanField()
    premium_contentUp = models.BooleanField()
    premium_responsive = models.BooleanField()
    premium_plugins = models.IntegerField()
    premium_productsUp = models.IntegerField()
    premium_ecommerc = models.BooleanField()
    premium_revisions = models.IntegerField()
    premium_price = models.FloatField()

    description = models.TextField()
    gallery_image = models.ImageField(upload_to="images/", null=True)
    gallery_extra_image = models.ImageField(upload_to="images/", null=True, blank=True)
    gallery_video = models.FileField(upload_to="videos/", null=True)


    gig_click_count = models.PositiveIntegerField(null=True, default=0)
    is_publish = models.BooleanField(default=False, null=True)

    # requirements = still thinking /.....

    def __str__(self):
        return self.title



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
    gig = models.ForeignKey(Gigs, on_delete=models.CASCADE, null=True)
    rate_seller = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)


