from django.contrib import admin
from main import models

# Register your models here.
admin.site.register([
    models.Question,
    models.choice,
    models.Answer,
])
