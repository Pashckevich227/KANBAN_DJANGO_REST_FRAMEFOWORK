from django.contrib import admin
from .models import *


admin.site.register(Board)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Mark)