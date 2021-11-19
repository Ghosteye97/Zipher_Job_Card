from django.contrib import admin
from .models import  jobCardsClass

# Register your models here.
class jobCardsAdmin(admin.ModelAdmin):
    pass

admin.site.register(jobCardsClass, jobCardsAdmin)

