from django.contrib import admin

from .models import Group, Question, Person

# Register your models here.
admin.site.register(Question)


admin.site.register(Group)
admin.site.register(Person)
