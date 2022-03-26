from django.contrib import admin

from .models import Group, Question

# Register your models here.
admin.site.register(Question)

#Dylan
admin.site.register(Group)