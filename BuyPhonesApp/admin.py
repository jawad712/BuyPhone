from django.contrib import admin
from .models import Mobile, Review, Specs

# Register your models here.

admin.site.register(Mobile)
admin.site.register(Specs)
admin.site.register(Review)