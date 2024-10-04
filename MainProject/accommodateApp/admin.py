from django.contrib import admin
from .models import Category,Manager,Product,PriceRange,Rooms,Amenities,ProductReview
# Register your models here.
admin.site.register(Category)
admin.site.register(Manager)
admin.site.register(Product)
admin.site.register(PriceRange)
admin.site.register(Rooms)
admin.site.register(Amenities)
admin.site.register(ProductReview)
