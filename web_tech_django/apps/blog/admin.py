from django.contrib import admin
from .models import Member, Tour, Hotel, OrderHotel
from .models import OrderTour, Customer
from .models import Bus, OrderBus

# Register your models here.
admin.site.register(Member)
admin.site.register(Tour)
admin.site.register(Customer)
admin.site.register(OrderTour)
admin.site.register(Hotel)
admin.site.register(OrderHotel)
admin.site.register(Bus)
admin.site.register(OrderBus)