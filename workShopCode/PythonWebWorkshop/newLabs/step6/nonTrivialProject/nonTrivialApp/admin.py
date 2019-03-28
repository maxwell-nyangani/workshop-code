from django.contrib import admin
from nonTrivialApp.models import Store, Customer, Tag, Purchase, PurchaseItem, Delivery, Address, Product

# Register your models here.
admin.site.register(Store)
admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)
admin.site.register(Delivery)
admin.site.register(Address)
admin.site.register(Product)
