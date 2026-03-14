from django.contrib import admin
from .models import Question, Option
from .models import Character
from .models import VerseCard

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Character)
admin.site.register(VerseCard)
