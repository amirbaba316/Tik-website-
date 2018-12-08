from django.contrib import admin
from problem.models import Problem
from Discussion.models import Discussion,Comments

# Register your models here.

admin.site.register(Discussion)
admin.site.register(Comments)
