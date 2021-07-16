from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


# class SellerAccount(admin.StackedInline):
#     model = ExtendedUser
#     can_delete = False


# class UserAdmin(BaseUserAdmin):
#     inlines = (SellerAccount,)
#     list_display = ('username',)




# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.unregister(ExtendedUser)
admin.site.register(ExtendedUser)
admin.site.register(Services)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Tag)
admin.site.register(DeliveryTime)
admin.site.register(Gigs)
admin.site.register(PostRequestModel)
admin.site.register(Currency)
admin.site.register(DummyUser)
admin.site.register(LandingSlider)
