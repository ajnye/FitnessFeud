from django.contrib import admin

from .models import Group, Question, Person, Exercise

# Register your models here.
admin.site.register(Question)


admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Exercise)
