from django.contrib import admin

from .models import Expense
from .models import income

# Register your models here.
admin.site.register(Expense)

admin.site.register(income)
