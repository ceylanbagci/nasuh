from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Case)
admin.site.register(Client)
admin.site.register(Partner)
admin.site.register(Status)
admin.site.register(Partnership)