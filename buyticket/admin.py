from django.contrib import admin
from .models import party,Agent, Payment, TicketPrice
# Register your models here.

admin.site.register(party)
admin.site.register(Agent)
admin.site.register(Payment)
admin.site.register(TicketPrice)