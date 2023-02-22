from django.contrib import admin
from .models import Category, MenuItem, Cart, Order, OrderItem, Cur_User
# Register your models here.

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cur_User)
