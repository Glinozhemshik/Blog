from django.contrib import admin
from blog.models import Statya

class StatyaAdmin(admin.ModelAdmin):
    list_display = ("title", "time", "user")


admin.site.register(Statya)

