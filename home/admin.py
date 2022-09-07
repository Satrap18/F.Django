from django.contrib import admin
from . import models
from .models import Todo
# Register your models here.


admin.site.register(Todo)