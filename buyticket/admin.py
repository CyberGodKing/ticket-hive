from django.contrib import admin
from .models import party,Agent, Payment
# Register your models here.

admin.site.register(party)
admin.site.register(Agent)
admin.site.register(Payment)