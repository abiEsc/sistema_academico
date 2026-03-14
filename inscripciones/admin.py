from django.contrib import admin
from .models import Question, Option, Character, VerseCard, GeneralQuestion, GeneralOption

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Character)
admin.site.register(VerseCard)
admin.site.register(GeneralQuestion)
admin.site.register(GeneralOption)
