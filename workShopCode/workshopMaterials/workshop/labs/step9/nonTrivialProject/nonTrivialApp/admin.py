from django.contrib import admin
# Import your models here.
from nonTrivialApp.models import Store, Address, Customer, Delivery, Product, Purchase, PurchaseItem, Tag
# Register your models here.
admin.site.register(Store)  # This make your model accessible from admin portal
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Delivery)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)
admin.site.register(Tag)