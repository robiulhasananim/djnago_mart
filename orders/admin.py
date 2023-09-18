from django.contrib import admin
from .models import Payment, Order, OderProduct, PaymentGateWaySettings
# Register your models here.
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OderProduct)
admin.site.register(PaymentGateWaySettings)
