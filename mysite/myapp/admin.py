from django.contrib import admin

# Register your models here.

from .models import PhoneNumber
from .models import Patron

admin.site.register(PhoneNumber)
admin.site.register(Patron)
