from django.contrib import admin
from .models import Question, Option
from .models import Character

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Character)
